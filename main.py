from window import Line, Point, Window

def main():
    window = Window(800, 600)
    window.draw_line(Line(Point(50, 50), Point(80, 80)), "black")
    window.wait_for_close()

if __name__ == "__main__":
    main()
