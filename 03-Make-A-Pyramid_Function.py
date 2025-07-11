from mcpi.minecraft import Minecraft

SAND = 12

world = Minecraft.create()

def pyramid(n):
    pos = world.player.getTilePos()

    for i in range(1, n + 1):
        delta = 2 * n - (2 * (i - 1)) - 1
        h = i - 1
        world.setBlocks(pos.x + i, pos.y + h, pos.z + i,
                        pos.x + i + delta, pos.y + h, pos.z + i + delta,
                        SAND)

pyramid(3)

