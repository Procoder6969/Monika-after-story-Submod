# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="GlitcherOnYT",
        name="Custom Dialogue",
        description="This is custom dialogue for Monika After Story",
        version="1.0.0"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Custom Dialogue",
            user_name="GlitcherOnYT",
            repository_name="Custom Dialogue",
            update_dir="Submods",
            attachment_id=None
        )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_truthful",
            category=["misc"],
            prompt="I Hate You",
            pool=True,
            unlocked=True
        )
    )
    
label monika_truthful:

    $ mas_loseAffection(1000)

m 2wktso "Wh...WHAT!"
m 2wktsx "I th...thought that we were made for eachother"
m 2wfo "YOU KNOW WHAT I HATE YOU!!!"
m 2wftso "AND I HOPE TO NEVER SEE YOU AGAIN!!!"
m 2dfx "Fucking asshole"

label enableQuit:
    $ mas_enable_quit()
    $ renpy.quit()

    return