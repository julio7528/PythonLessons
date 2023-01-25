struct Point{
    int x;
    int y;
};

struct Point points[10];

struct Point points[3] = {{1,2}, {3,4}, {5,6}};

printf("x: %d, y: %d", points[0].x, points[0].y);