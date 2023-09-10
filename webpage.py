from taipy.gui import Gui, navigate


root_md="<|menu|label=Menu|lov={[('Add-Station', 'Add Station'), ('About-Us', 'About Us')]}|on_action=on_menu|>"
enter_details = "Enter any details here..."

def reset_box():
    enter_details = "Enter any details here..."


page1_md= """

# Where's My Water?

<|{"WhartonCampus.png"}|image|width="1000px"|height="1000px"|>

## Add a Fountain

### Notes ### {: .text-align:center;}

<|{enter_details}|input|>
#
<|Submit|button|on_action=reset_box|>

### Status ###

<|Working!|button|>
<|Not Functional|button|>
<|Not Clean|button|>
"""


page2_md="""## About Us

<|{"about_us.jpg"}|image|width=1000px|height=500px|>

"""


def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)


pages = {
    "/": root_md,
    "Page-1": page1_md,
    "About-Us": page2_md
}

Gui(pages=pages).run(favicon = "Favicon Final.png", title = "Where's My Water?", use_reloader=True)