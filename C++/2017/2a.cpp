#include <bits/stdc++.h>

using namespace std;

typedef unsigned int uint;
typedef long long ll;

#define F first
#define S second

const int INF = INT_MAX;

struct Player {
    int p;
    int m;

    void increase_pos(int n){
        p = (p + n) % 36;
        if (p == 0) p = 36;
    }
};

struct Grid {
    bool x_lines[6][6] = {0};
    bool y_lines[6][6] = {0};

    int boxes[5][5] = {0};

    bool found_box;

    bool check_square(int x, int y) {
        // 0 < x < 5, 0 < y < 5
        return x_lines[x][y] && x_lines[x+1][y] && y_lines[x][y] && y_lines[x][y + 1];
    }

    bool try_up(int x, int y, int player){
        if (!y_lines[x-1][y] && x > 0){ // Check up
            y_lines[x-1][y] = true;
            if (check_square(x-1, y-1)){
                boxes[x-1][y-1] = player;
                found_box = true;
            }
            if (check_square(x-1, y)){
                boxes[x-1][y] = player;
                found_box = true;
            }
            return true;
        }
        return false;
    }

    bool try_right(int x, int y, int player){
        if (!x_lines[x][y] && y < 5){ // Check right
            x_lines[x][y] = true;
            if (check_square(x-1, y)){
                boxes[x-1][y] = player;
                found_box = true;
            }
            if (check_square(x, y)){
                boxes[x][y] = player;
                found_box = true;
            }
            return true;
        }
        return false;
    }

    bool try_down(int x, int y, int player){
        if (!y_lines[x][y] && x < 5){ // Check down
            y_lines[x][y] = true;
            if (check_square(x, y)){
                boxes[x][y] = player;
                found_box = true;
            }
            if (check_square(x, y-1)){
                boxes[x][y-1] = player;
                found_box = true;
            }
            return true;
        }
        return false;
    }

    bool try_left(int x, int y, int player){
        if (!x_lines[x][y-1] && y > 0){ // Check left
            x_lines[x][y-1] = true;
            if (check_square(x, y-1)){
                boxes[x][y-1] = player;
                found_box = true;
            }
            if (check_square(x-1, y-1)){
                boxes[x-1][y-1] = player;
                found_box = true;
            }
            return true;
        }
        return false;
    }

    bool attempt_draw(int pos, int player){
        int x = ceil((float)pos/(float)6) - 1;
        int y = (pos % 6 + 5) % 6 ;
        if (player == 1){
            if (try_up(x, y, 1)) return true;
            if (try_right(x, y, 1)) return true;
            if (try_down(x, y, 1)) return true;
            if (try_left(x, y, 1)) return true;
        } else {
            if (try_up(x, y, 2)) return true;
            if (try_left(x, y, 2)) return true;
            if (try_down(x, y, 2)) return true;
            if (try_right(x, y, 2)) return true;           
        }
        
        return false;
    }

    void show_grid(){
        for (int i = 0; i < 6; i++){
            for (int j = 0; j < 6; j++){
                cout << 'o';
                if (x_lines[i][j]) cout << '-';
                else cout << ' ';
            }
            cout << endl;
            for (int j = 0; j < 6; j++){
                if (y_lines[i][j]) cout << '|';
                else cout << ' ';
                cout << ' ';
            }
            cout << endl;
        }
    }
};

int main() {
    Player a, b; 
    int t;
    cin >> a.p >> a.m >> b.p >> b.m >> t;
    
    Grid g;

    bool player_one = true;
    for (int i = 0; i < t; i++){
        bool moved = false;
        if (player_one){
            // Player 1 to move
            a.increase_pos(a.m);
            // Attempt to draw line on new node
            moved = g.attempt_draw(a.p, 1);
            while (!moved){
                a.increase_pos(1);
                moved = g.attempt_draw(a.p, 1);
            }
        } else {
            // Player 2 to move
            b.increase_pos(b.m);
            // Attempt to draw line on new node
            moved = g.attempt_draw(b.p, 2);
            while (!moved){
                b.increase_pos(1);
                moved = g.attempt_draw(b.p, 2);
            }
        }
        if (!g.found_box) player_one = !player_one;
        else g.found_box = false;
    }

    int p1_squares = 0, p2_squares = 0;
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++){
            if (g.boxes[i][j] == 0) cout << '*';
            else if (g.boxes[i][j] == 1){
                cout << 'X';
                p1_squares++;
            }
            else if (g.boxes[i][j] == 2){
                cout << 'O';
                p2_squares++;
            }
        }
        cout << "\n";
    }
    cout << p1_squares << " " << p2_squares;
}