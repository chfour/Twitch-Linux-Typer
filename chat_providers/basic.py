class Chat:
    name = "Basic input() chat provider"
    
    async def get_message(self) -> str:
        return input(">")
