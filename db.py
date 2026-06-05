import aiosqlite

DB = "bot.db"


async def init_db():
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT DEFAULT 'NoName',
            status TEXT DEFAULT 'new',
            xp INTEGER DEFAULT 0,
            warns INTEGER DEFAULT 0
        )
        """)
        await db.commit()


async def add_user(user_id: int):
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
        INSERT OR IGNORE INTO users (user_id)
        VALUES (?)
        """, (user_id,))
        await db.commit()


async def set_name(user_id: int, name: str):
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
        UPDATE users SET name=?
        WHERE user_id=?
        """, (name, user_id))

        await db.commit()


async def get_user(user_id: int):
    async with aiosqlite.connect(DB) as db:
        async with db.execute("""
        SELECT name, status, xp, warns FROM users WHERE user_id=?
        """, (user_id,)) as cur:
            return await cur.fetchone()


async def add_xp(user_id: int, amount: int):
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
        UPDATE users SET xp = xp + ?
        WHERE user_id=?
        """, (amount, user_id))
        await db.commit()


async def warn_user(user_id: int):
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
        UPDATE users SET warns = warns + 1
        WHERE user_id=?
        """, (user_id,))
        await db.commit()
