from taipy.gui import Gui, navigate


root_md="<|menu|label=Menu|lov={[('Page-1', 'Page 1'), ('Page-2', 'Page 2')]}|on_action=on_menu|>"
enter_details = "Enter any details here..."
page1_md= """

# Welcome to Where's My Water?

<|{"Wharton Campus.png"}|image|width="1000px"|height="1000px"|>

## Add a Fountain

### Notes ### {: .text-align:center;}

<|{enter_details}|input|>
#
<|Submit|button|>

### Status ###

<|Working!|button|>
<|Not Functional|button|>
<|Not Clean|button|>
"""




page2_md="## This is page 4"


def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)


pages = {
    "/": root_md,
    "Page-1": page1_md,
    "Page-2": page2_md
}

Gui(pages=pages).run(use_reloader=True)