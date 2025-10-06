from mcpi.minecraft import Minecraft

OBSIDIAN = 49
AIR = 0
FIRE = 51

world = Minecraft.create()

def portal(width, height):
    pos = world.player.getPos()

    world.setBlocks(pos.x, pos.y, pos.z,
                    pos.x + width - 1, pos.y + height - 1, pos.z,
                    OBSIDIAN)

    world.setBlocks(pos.x + 1, pos.y + 1, pos.z,
                    pos.x + width - 2, pos.y + height - 2, pos.z,
                    AIR)

    world.setBlock(pos.x + 1, pos.y + 1, pos.z, FIRE)

portal(4, 5)




