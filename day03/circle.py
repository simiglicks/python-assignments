import argparse

def circle(radius=None):
    if not radius:
        parser = argparse.ArgumentParser()
        parser.add_argument('radius', type=int)
        args = parser.parse_args()
        radius = args.radius
    area= 3.14*(radius**2)
    circumference= 3.14*(2*radius)
    print(area)
    print(circumference)

# check if file was run instead of imported
if __name__ == '__main__':
    circle()