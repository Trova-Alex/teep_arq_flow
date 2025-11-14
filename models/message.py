from queue import Queue


class Message:

    def __init__(self, index: str, cmd: str, args: str, kwargs: dict, reply_q: Queue):
        self.index = index
        self.cmd = cmd,
        self.args = args
        self.kwargs = kwargs
        self.reply_q = reply_q