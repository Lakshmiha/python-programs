from Graphics.Circle import circlearea
from Graphics.Rectangle import rectarea
from Graphics.ThreeDGraphics.Cuboid import cubarea
from Graphics.ThreeDGraphics.Sphere import spherearea

print("Area and perimeter of circle and rectangle:")
print("Rectangle(length=5,breadth=3) and circle(radius=6):",rectarea.perimeter(5,3),rectarea.area(5,3),circlearea.perimeter(6),circlearea.area(6))

print("Area and perimeter of sphere  and cuboid:")
print("Sphere(radius=6) and Cuboid(length=5,breadth=3,height=6):",spherearea.sphere_perimeter(6),spherearea.sphere_area(6),cubarea.cuboid_perimeter(5,3,6),cubarea.cuboid_area(5,3,6))

      
