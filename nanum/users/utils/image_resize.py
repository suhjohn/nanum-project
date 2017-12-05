from io import BytesIO

from PIL import Image as pil

__all__ = (
    'user_img_path',
    'user_thumb_img_200_path',
    'user_thumb_img_50_path',
    'user_thumb_img_25_path',
    'rescale',
)


def user_img_path(instance, filename):
    # 업로드 이미지 file 저장 경로
    return f'profile/img/{instance.user.__str__()}/{filename}'


def user_thumb_img_200_path(instance, filename):
    # 200 * 200 썸네일 이미지 file 저장 경로
    return f'profile/thumbnail_img_200/{instance.user.__str__()}/{filename}'


def user_thumb_img_50_path(instance, filename):
    # 50 * 50 썸네일 이미지 file 저장 경로
    return f'profile/thumbnail_img_50/{instance.user.__str__()}/{filename}'


def user_thumb_img_25_path(instance, filename):
    # 25 * 25 썸네일 이미지 file 저장 경로
    return f'profile/thumbnail_img_25/{instance.user.__str__()}/{filename}'


def rescale(data, width, height, force=True):
    """

    :param data: Image Byte Data
    :param width: 원하는 가로 길이
    :param height: 원하는 세로 길이
    :param force: True일 경우, 가로 세로 비율 맞게, False일 경우 max값에 맞게 thumbnail화
    :return:
    """
    max_width = width
    max_height = height

    # input_file = BytesIO(data.read())
    input_file = BytesIO(data)
    img = pil.open(input_file)

    # RGBA, A(투명도)를 포함한 PNG와 같은 파일이 올 경우, 이를 변환함
    if img.mode != 'RGB':
        img = img.convert('RGB')

    if not force:
        img.thumbnail((max_width, max_height), pil.ANTIALIAS)
    else:
        src_width, src_height = img.size
        src_ratio = float(src_width) / float(src_height)
        dst_width, dst_height = max_width, max_height
        dst_ratio = float(dst_width) / float(dst_height)

        if dst_ratio < src_ratio:
            crop_height = src_height
            crop_width = crop_height * dst_ratio
            x_offset = int(src_width - crop_width) // 2
            y_offset = 0
        else:
            crop_width = src_width
            crop_height = crop_width / dst_ratio
            x_offset = 0
            y_offset = int(src_height - crop_height) // 3
        img = img.crop((x_offset, y_offset, x_offset + int(crop_width), y_offset + int(crop_height)))
        img = img.resize((dst_width, dst_height), pil.ANTIALIAS)

    image_file = BytesIO()
    img.save(image_file, 'JPEG')
    return image_file
