char c = 'Q';
int HEIGHT = 500;
int HALF = HEIGHT / 2;
int QUART = HEIGHT / 4;
PFont fira;
color colr = color(255, 255, 255, 50);

void setup() {
    size(500, 500);
    background(0);
    fira = createFont("FiraCode-Regular.otf", QUART);
    smooth(2);
}

void draw() {
    textSize(QUART);
    textAlign(CENTER, CENTER);
    text(c, HALF, HALF);
    float value = alpha(colr);
    fill(value);
}
