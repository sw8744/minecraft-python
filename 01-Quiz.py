from mcpi.minecraft import Minecraft
world = Minecraft.create()

msg = input("메시지를 입력하세요: ")
world.postToChat(msg)

