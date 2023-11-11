class CBotSettings:
    # Your Discord bot token goes here
    TOKEN = "YOUR DISCORD TOKEN HERE"
    # What channel should the bot log admin/mod actions it performs to?
    CHANNEL_ID = 0000000000000000000
    # Which character should we use to trigger a command?
    CommandSymbol = "$"
    # Should we archive images?
    ArchiveImages = False
    # If `ArchiveImages` is enabled, which channels should we archive?
    ArchiveChannels = [
        "general",
        "memes"
        ]
    # Where do we store our images? This MUST have a trailing /
    ArchiveRoot = "/home/exile/Pictures/CunnyBot"
    # The name of our database file. Must be store in bot root.
    DbName = "db.sql"