import motor.motor_asyncio
import asyncio


class MotorHandler:
    def __init__(self, db_user, db_pass, database, collection):
        conn_str = "mongodb+srv://{}:{}@cluster0.hao7p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(
            db_user, db_pass
        )
        loop = asyncio.get_event_loop()
        print(conn_str)
        self.bd_client = loop.run_until_complete(
            self.get_server_info(conn_str)
        )
        self.database = self.bd_client[database]
        self.collection = self.database[collection]

    async def get_server_info(self, conn_str: str):
        client = motor.motor_asyncio.AsyncIOMotorClient(
            conn_str, serverSelectionTimeoutMS=5000
        )
        try:
            print(await client.server_info())
            return client
        except Exception as e:
            print("Unable to connect to the server --> {}".format(e))

    def insert(self, user, value=0):
        loop = self.bd_client.get_io_loop()

        result = loop.run_until_complete(self.do_find_one(user))
        if result == None:
            result = loop.run_until_complete(self.do_insert_one(user, value))
            return result

        return False

    async def do_insert_one(self, user, value):
        document = {"user": user, "value": value}
        result = await self.collection.insert_one(document)
        return result

    def get(self, user):
        loop = self.bd_client.get_io_loop()
        result = loop.run_until_complete(self.do_find_one(user))
        return result

    async def do_find_one(self, user):
        result = await self.collection.find_one(
            {"user": user}, {"_id": 0, "user": 0}
        )
        return result["value"]

    def delete(self, user):
        loop = self.bd_client.get_io_loop()
        result = loop.run_until_complete(self.do_delete_one(user))
        return result

    async def do_delete_one(self, user):
        result = await self.collection.delete_one({"user": user})
        return result

    def increment(self, user, increment=1):
        loop = self.bd_client.get_io_loop()
        result = loop.run_until_complete(
            self.do_increment_one(user, increment)
        )
        return result

    async def do_increment_one(self, user, increment):
        old_document = await self.collection.find_one({"user": user})
        if old_document == None:
            return False

        _id = old_document["_id"]
        new_value = old_document["value"] + increment
        result = await self.collection.replace_one(
            {"_id": _id}, {"user": user, "value": new_value}
        )
        return result

    def get_all_users(self):
        loop = self.bd_client.get_io_loop()
        result = loop.run_until_complete(self.do_find_all())
        return result

    async def do_find_all(self):
        users_list = []
        async for document in self.collection.find({"value": {"$gt": 0}}):
            users_list.append(document["user"])

        return users_list
