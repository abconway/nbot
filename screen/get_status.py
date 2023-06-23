from PIL import Image

from config import config


def get_box(ref_loc, global_offset, offset, num_width, num_height):
    return (
        ref_loc[0] + global_offset[0] + offset[0],
        ref_loc[1] + global_offset[1] + offset[1], 
        ref_loc[0] + global_offset[0] + offset[0] + num_width, 
        ref_loc[1] + global_offset[1] + offset[1] + num_height,
    )


def get_status_images(im: Image, ref_loc, in_battle=False, icon_size='32x32'):
    if in_battle:
        battle_status = 'in_battle'
    else:
        battle_status = 'out_of_battle'

    num_width = config['icon_sizes'][icon_size]['numbers']['width']
    num_height = config['icon_sizes'][icon_size]['numbers']['height']

    hp1_offset = config['icon_sizes'][icon_size]['status']['hp1_offset']
    hp2_offset = config['icon_sizes'][icon_size]['status']['hp2_offset']
    hp3_offset = config['icon_sizes'][icon_size]['status']['hp3_offset']

    mp1_offset = config['icon_sizes'][icon_size]['status']['mp1_offset']
    mp2_offset = config['icon_sizes'][icon_size]['status']['mp2_offset']
    mp3_offset = config['icon_sizes'][icon_size]['status']['mp3_offset']

    p1_global_offset = config['icon_sizes'][icon_size]['status']['global_offset'][battle_status]['p1']
    p2_global_offset = config['icon_sizes'][icon_size]['status']['global_offset'][battle_status]['p2']
    p3_global_offset = config['icon_sizes'][icon_size]['status']['global_offset'][battle_status]['p3']
    
    box_p1_hp1 = get_box(ref_loc, p1_global_offset, hp1_offset, num_width, num_height)
    box_p1_hp2 = get_box(ref_loc, p1_global_offset, hp2_offset, num_width, num_height)
    box_p1_hp3 = get_box(ref_loc, p1_global_offset, hp3_offset, num_width, num_height)
    
    im_p1_hp1 = im.crop(box_p1_hp1)
    im_p1_hp2 = im.crop(box_p1_hp2)
    im_p1_hp3 = im.crop(box_p1_hp3)

    box_p1_mp1 = get_box(ref_loc, p1_global_offset, mp1_offset, num_width, num_height)
    box_p1_mp2 = get_box(ref_loc, p1_global_offset, mp2_offset, num_width, num_height)
    box_p1_mp3 = get_box(ref_loc, p1_global_offset, mp3_offset, num_width, num_height)

    im_p1_mp1 = im.crop(box_p1_mp1)
    im_p1_mp2 = im.crop(box_p1_mp2)
    im_p1_mp3 = im.crop(box_p1_mp3)

    box_p2_hp1 = get_box(ref_loc, p2_global_offset, hp1_offset, num_width, num_height)
    box_p2_hp2 = get_box(ref_loc, p2_global_offset, hp2_offset, num_width, num_height)
    box_p2_hp3 = get_box(ref_loc, p2_global_offset, hp3_offset, num_width, num_height)

    im_p2_hp1 = im.crop(box_p2_hp1)
    im_p2_hp2 = im.crop(box_p2_hp2)
    im_p2_hp3 = im.crop(box_p2_hp3)

    box_p2_mp1 = get_box(ref_loc, p2_global_offset, mp1_offset, num_width, num_height)
    box_p2_mp2 = get_box(ref_loc, p2_global_offset, mp2_offset, num_width, num_height)
    box_p2_mp3 = get_box(ref_loc, p2_global_offset, mp3_offset, num_width, num_height)

    im_p2_mp1 = im.crop(box_p2_mp1)
    im_p2_mp2 = im.crop(box_p2_mp2)
    im_p2_mp3 = im.crop(box_p2_mp3)

    box_p3_hp1 = get_box(ref_loc, p3_global_offset, hp1_offset, num_width, num_height)
    box_p3_hp2 = get_box(ref_loc, p3_global_offset, hp2_offset, num_width, num_height)
    box_p3_hp3 = get_box(ref_loc, p3_global_offset, hp3_offset, num_width, num_height)

    im_p3_hp1 = im.crop(box_p3_hp1)
    im_p3_hp2 = im.crop(box_p3_hp2)
    im_p3_hp3 = im.crop(box_p3_hp3)

    box_p3_mp1 = get_box(ref_loc, p3_global_offset, mp1_offset, num_width, num_height)
    box_p3_mp2 = get_box(ref_loc, p3_global_offset, mp2_offset, num_width, num_height)
    box_p3_mp3 = get_box(ref_loc, p3_global_offset, mp3_offset, num_width, num_height)

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