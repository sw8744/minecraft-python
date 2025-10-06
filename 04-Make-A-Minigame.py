from mcpi.minecraft import Minecraft
import time

SNOW = 80
RANGE = 10
FALLING_TIME = 0.3

world = Minecraft.create()
START_POS = world.player.getTilePos()

def fall_block():
    pos = world.player.getTilePos()
    if world.getBlock(pos.x, pos.y - 1, pos.z) == SNOW:
        time.sleep(FALLING_TIME)
        world.setBlock(pos.x, pos.y - 1, pos.z, 0)

def check_block():
    for i in range(0, RANGE + 1):
        for j in range(0, RANGE + 1):
            if world.getBlock(START_POS.x + i, START_POS.y + 10, START_POS.z + j) != SNOW:
                return False
    return True

def check_y():
    pos = world.player.getTilePos()
    if pos.y < START_POS.y + 10:
        return False
    return True

world.postToChat("게임을 시작합니다.")
world.player.setTilePos(START_POS.x, START_POS.y + 10, START_POS.z)
pos = world.player.getTilePos()
world.setBlocks(pos.x, pos.y - 1, pos.z,
                pos.x + RANGE, pos.y - 1, pos.z + RANGE,
                SNOW)
world.setBlock(pos.x, pos.y - 1, pos.z, 1)

while True:
    fall_block()
    if check_block():
        world.postToChat("게임을 종료합니다.")
        break
    if not check_y():
        world.postToChat("떨어졌습니다. 게임을 종료합니다.")
        world.setBlocks(START_POS.x, START_POS.y + 9, START_POS.z,
                        START_POS.x + RANGE, START_POS.y + 9, START_POS.z + RANGE,
                        0)
        break

