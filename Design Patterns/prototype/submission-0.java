interface Shape {
    Shape clone();
}

class Rectangle implements Shape {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int getWidth() {
        return this.width;
    }

    public int getHeight() {
        return this.height;
    }

    @Override
    public Shape clone() {
        Shape clone = new Rectangle(this.width, this.height);
        return clone;
    }
}

class Square implements Shape {
    private int length;

    public Square(int length) {
        this.length = length;
    }

    public int getLength() {
        return this.length;
    }

    @Override
    public Shape clone() {
        Square clone = new Square(this.length);
        return clone;
    }
}

class Test {
    public List<Shape> cloneShapes(List<Shape> shapes) {
        List<Shape> clones = new ArrayList<>();
        for (Shape shape : shapes) {
            clones.add(shape.clone());
        }
        return clones;
    }
}
