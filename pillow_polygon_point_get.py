from tkinter import *
from PIL import Image, ImageTk, ImageDraw

def on_canvas_click(event):
    global clicked_points

    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    clicked_points.append((x, y))
    print(f"Clicked coordinates: {x}, {y}")

    # TODO 点の数 [清田:12, 札幌南部:16, 札幌北部:24, 厚別:12, 江別:12, 長沼:14, 恵庭:8]
    if len(clicked_points) >= 12: 
        draw_polygon()

def draw_polygon():
    global image, canvas, photo, clicked_points

    color = (255, 0, 0)

    draw = ImageDraw.Draw(image)
    draw.polygon(clicked_points, fill=color, outline=color)

    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=NW, image=photo)

    print(f"Polygon coordinates: {clicked_points}")

    clicked_points = []

def main():
    global image, canvas, photo, clicked_points

    # なにも色がついていない画像
    # image = Image.open("original_image.png")
    
    # 往路のデフォルメマップ
    # image = Image.open("map_before.png")

    # 復路のデフォルメマップ
    image = Image.open("map_after.png")

    # 吹き出しのTempalte
    # image = Image.open("map_after_transparent.png")

    # 一覧画像 車
    # image = Image.open("③試合前_黒_混雑表示イメージFIX.png")

    # 一覧画像 鉄道
    # image = Image.open("map_after_transparent.png")

    clicked_points = []

    root = Tk()
    root.title("Polygon Drawing")

    canvas_frame = Frame(root)
    canvas_frame.pack(side=LEFT, fill=BOTH, expand=True)

    h_scroll = Scrollbar(canvas_frame, orient="horizontal")
    h_scroll.pack(side=BOTTOM, fill=X)

    v_scroll = Scrollbar(canvas_frame, orient="vertical")
    v_scroll.pack(side=RIGHT, fill=Y)

    canvas = Canvas(canvas_frame, width=root.winfo_screenwidth()//2, height=root.winfo_screenheight()//2, 
                    scrollregion=(0, 0, image.width, image.height), xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    h_scroll.config(command=canvas.xview)
    v_scroll.config(command=canvas.yview)

    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.bind("<Button-1>", on_canvas_click)

    root.mainloop()

if __name__ == "__main__":
    main()
