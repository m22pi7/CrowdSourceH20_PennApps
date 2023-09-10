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


#####Sustainability plays a pivotal role in addressing the Earth's changing climate, representing a critical strategy for mitigating the impact of global climate change. As our planet faces escalating challenges such as rising temperatures, more frequent extreme weather events, and threats to biodiversity, sustainability principles guide us toward responsible and ethical practices. By adopting sustainable practices in areas like energy generation, transportation, agriculture, and resource management, we can reduce greenhouse gas emissions, conserve natural resources, and protect ecosystems. Sustainability promotes resilience in the face of climate-related challenges, ensuring that future generations can enjoy a stable and habitable planet. It emphasizes the need to balance human activities with the capacity of the Earth's systems, fostering a harmonious relationship between society and the environment. In essence, sustainability serves as a compass guiding humanity toward a more environmentally conscious and climate-resilient future.

## Why Water Bottle Stations?

<|{"LARQ.jpg"}|image|width=1000px|height=600px|>

##### Both of us our avid water bottle enthusiasts, and enjoy trying all sorts of different types of ways to consume water. However, after researching the LARQ water bottle we realized "self-cleaning" bottles were the way to go! We look forward to sharing our equal passion for the environment and water with the world with this "Where's My Water?" project.

This project was created by Manuj Marwaha and Mudit Marwaha for Penn Apps 2023 utilizing the Taipy Library

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