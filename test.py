import asyncio
import traceback
from pprint import pprint

from devtools import debug

from mirai import (
    At,
    ExternalEvents, 
    Face,
    FriendMessage,
    GroupMessage,
    Image,
    MessageContextBody,
    Plain,
    QQFaces,
    Session,
    UnexceptedException,
    ImageType,
    Direct
)
from mirai.event import external

from context_test import is_startwith

async def main():
    authKey = "213we355gdfbaerg"
    qq = 208924405

    print("???")
    async with Session(f"mirai://localhost:8070/?authKey={authKey}&qq={qq}") as session:
        print(session.enabled)

        """
        @session.receiver(GroupMessage)
        async def normal_handle(context):
            if isinstance(context.message, GroupMessage):

                print(f"[{context.message.sender.group.id}][{context.message.sender.id}]:", context.message.messageChain.toString())
                #debug(context)
                if context.message.messageChain.toString().startswith("/raiseAnother"):
                    raise ValueError("fa")
                elif context.message.messageChain.toString().startswith("/raise"):
                    raise Exception("test")
                elif context.message.messageChain.toString().startswith("/test-at"):
                    await context.session.sendGroupMessage(
                        context.message.sender.group.id,
                        [
                            At(target=context.message.sender.id),
                            Plain(text="meow"),
                            Face(faceId=QQFaces["jingkong"])
                        ]
                    )
                elif context.message.messageChain.toString().startswith("/test-localimage"):
                    await context.session.sendGroupMessage(
                        context.message.sender.group.id,
                        [
                            await Image.fromFileSystem("2019-05-04_15.52.03.png", session, ImageType.Group),
                            Plain(text="faq")
                        ]
                    )
                elif context.message.messageChain.toString().startswith("/muteMe"):
                    await context.session.mute(
                        context.message.sender.group.id,
                        context.message.sender.id,
                        60
                    )
                    await asyncio.sleep(5)
                    await context.session.unmute(
                        context.message.sender.group.id,
                        context.message.sender.id
                    )
                elif context.message.messageChain.toString().startswith("/replyMe"):
                    debug(await context.session.sendGroupMessage(
                        context.message.sender.group.id,
                        "reply da!",
                        quoteSource=context.message.messageChain.getSource()
                    ))
                if context.message.messageChain.hasComponent(Image):
                    pass

        @session.receiver(ExternalEvents.MemberMuteEvent)
        @session.receiver(external.BotMuteEvent)
        async def _(context):
            debug(context)

        @session.exception_handler(UnexceptedException)
        async def exception_handle(context: UnexceptedException):
            debug(context)
        """
        @session.receiver(GroupMessage)
        async def normal_handle(context):
            if is_startwith("/"):
                await context.session.sendGroupMessage(
                    context.message.sender.group.id,
                    [Plain(text="嗯?你刚才以斜杠开头写了什么啊")]
                )

        await session.joinMainThread()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    exit()
