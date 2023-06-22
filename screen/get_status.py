from PIL import Image

from config import config


def get_status_images(im: Image, in_battle=False, resolution='1920x1080'):
    if in_battle:
        battle_status = 'in_battle'
    else:
        battle_status = 'out_of_battle'
    
    box_p1_hp1 = config['resolutions'][resolution][battle_status]['status']['p1']['hp1']
    box_p1_hp2 = config['resolutions'][resolution][battle_status]['status']['p1']['hp2']
    box_p1_hp3 = config['resolutions'][resolution][battle_status]['status']['p1']['hp3']
    im_p1_hp1 = im.crop(box_p1_hp1)
    im_p1_hp2 = im.crop(box_p1_hp2)
    im_p1_hp3 = im.crop(box_p1_hp3)
    
    box_p1_mp1 = config['resolutions'][resolution][battle_status]['status']['p1']['mp1']
    box_p1_mp2 = config['resolutions'][resolution][battle_status]['status']['p1']['mp2']
    box_p1_mp3 = config['resolutions'][resolution][battle_status]['status']['p1']['mp3']
    im_p1_mp1 = im.crop(box_p1_mp1)
    im_p1_mp2 = im.crop(box_p1_mp2)
    im_p1_mp3 = im.crop(box_p1_mp3)

    box_p2_hp1 = config['resolutions'][resolution][battle_status]['status']['p2']['hp1']
    box_p2_hp2 = config['resolutions'][resolution][battle_status]['status']['p2']['hp2']
    box_p2_hp3 = config['resolutions'][resolution][battle_status]['status']['p2']['hp3']
    im_p2_hp1 = im.crop(box_p2_hp1)
    im_p2_hp2 = im.crop(box_p2_hp2)
    im_p2_hp3 = im.crop(box_p2_hp3)
    
    box_p2_mp1 = config['resolutions'][resolution][battle_status]['status']['p2']['mp1']
    box_p2_mp2 = config['resolutions'][resolution][battle_status]['status']['p2']['mp2']
    box_p2_mp3 = config['resolutions'][resolution][battle_status]['status']['p2']['mp3']
    im_p2_mp1 = im.crop(box_p2_mp1)
    im_p2_mp2 = im.crop(box_p2_mp2)
    im_p2_mp3 = im.crop(box_p2_mp3)

    box_p3_hp1 = config['resolutions'][resolution][battle_status]['status']['p3']['hp1']
    box_p3_hp2 = config['resolutions'][resolution][battle_status]['status']['p3']['hp2']
    box_p3_hp3 = config['resolutions'][resolution][battle_status]['status']['p3']['hp3']
    im_p3_hp1 = im.crop(box_p3_hp1)
    im_p3_hp2 = im.crop(box_p3_hp2)
    im_p3_hp3 = im.crop(box_p3_hp3)
    
    box_p3_mp1 = config['resolutions'][resolution][battle_status]['status']['p3']['mp1']
    box_p3_mp2 = config['resolutions'][resolution][battle_status]['status']['p3']['mp2']
    box_p3_mp3 = config['resolutions'][resolution][battle_status]['status']['p3']['mp3']

    im_p3_mp1 = im.crop(box_p3_mp1)
    im_p3_mp2 = im.crop(box_p3_mp2)
    im_p3_mp3 = im.crop(box_p3_mp3)

    return (
        im_p1_hp1,
        im_p1_hp2,
        im_p1_hp3,
        im_p1_mp1,
        im_p1_mp2,
        im_p1_mp3,
        im_p2_hp1,
        im_p2_hp2,
        im_p2_hp3,
        im_p2_mp1,
        im_p2_mp2,
        im_p2_mp3,
        im_p3_hp1,
        im_p3_hp2,
        im_p3_hp3,
        im_p3_mp1,
        im_p3_mp2,
        im_p3_mp3,
    )