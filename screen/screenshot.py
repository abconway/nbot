from ctypes import windll

from PIL import Image
import win32gui
import win32ui


def get_screenshot() -> Image:
    window_handle = win32gui.FindWindow(None, 'NEStalgia | The Time Lords')
    windll.user32.SetProcessDPIAware()
    left, top, right, bottom = win32gui.GetClientRect(window_handle)
    width = right - left
    height = bottom - top

    # Create the necessary device contexts
    window_handle_dc = win32gui.GetWindowDC(window_handle)
    window_compatible_dc = win32ui.CreateDCFromHandle(window_handle_dc)
    window_target_dc = window_compatible_dc.CreateCompatibleDC()

    # Create a bitmap object
    target_bitmap = win32ui.CreateBitmap()
    target_bitmap.CreateCompatibleBitmap(window_compatible_dc, width, height)
    window_target_dc.SelectObject(target_bitmap)

    # Copy the screen into our bitmap object
    result = windll.user32.PrintWindow(window_handle, window_target_dc.GetSafeHdc(), 1)

    # Get the bitmap data
    bitmap_info = target_bitmap.GetInfo()
    bitmap_str = target_bitmap.GetBitmapBits(True)

    # Turn the bitmap into a PIL Image
    im = Image.frombuffer(
        'RGB',
        (bitmap_info['bmWidth'], bitmap_info['bmHeight']),
        bitmap_str, 
        'raw', 
        'BGRX', 
        0, 
        1,
    )

    # Clean up
    win32gui.DeleteObject(target_bitmap.GetHandle())
    window_target_dc.DeleteDC()
    window_compatible_dc.DeleteDC()
    win32gui.ReleaseDC(window_handle, window_handle_dc)

    return im


if __name__ == '__main__':
    get_screenshot().save('test.png')
