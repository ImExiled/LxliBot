class CBotSettings:
    # Your Discord bot token goes here
    TOKEN = "YOUR DISCORD TOKEN HERE"
    # Should we archive images?
    ArchiveImages = False
    # If `ArchiveImages` is enabled, which channels should we archive?
    ArchiveChannels = [
        "general",
        "memes"
        ]
    # If `ArchiveImages` is enabled, should we sort these images by folder?
    SortArchived = True