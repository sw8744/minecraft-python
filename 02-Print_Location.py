from mcpi.minecraft import Minecraft

world = Minecraft.create()

while True:
    pos = world.player.getTilePos()
    x = str(pos.x)
    y = str(pos.y)
    z = str(pos.z)
    world.postToChat("x: " + x + ", y: " + y + ", z: " + z)

