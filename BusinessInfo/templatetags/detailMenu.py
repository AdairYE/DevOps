from django import template
from BusinessInfo.models import product,project

register = template.Library()

@register.inclusion_tag("productManage/inclusion/detail-menu.html")
def get_business_info(request,productID):
    if productID == "all":
        Current = "所有项目"
    else:
        Current=product.objects.get(id=productID)
    starProduct = product.objects.filter(star=request.user).order_by('-id')
    productData = {
        "starProduct": starProduct,
        "user_CreateProduct": product.objects.filter(productOwner=request.user).exclude(id__in=starProduct).order_by(
            "-id"),
        "user_PartProject": product.objects.filter(participator=request.user).exclude(id__in=starProduct).order_by(
            "-id")
    }

    return {"productData":productData,"Current":Current}