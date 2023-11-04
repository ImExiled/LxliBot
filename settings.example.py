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
    # If `ArchiveImages` is enabled, should we sort these images by folder?
    SortArchived = True