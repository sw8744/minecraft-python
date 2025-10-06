from mcpi.minecraft import Minecraft

SAND = 12

world = Minecraft.create()

def pyramid(f):
    pos = world.player.getTilePos()

    for i in range(1, f + 1):
        delta = 2 * (f - (i - 1)) - 1

        world.setBlocks(pos.x + i - 1, pos.y + i - 1, pos.z + i - 1,
                        pos.x + i + delta, pos.y + i - 1, pos.z + i + delta,
                        SAND)

pyramid(3)

