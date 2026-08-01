# QairtApi - Qualcomm AI Runtime (QAIRT) SDK

# QairtApi

Updated:  Jul 02, 2026 80-63442-10  Rev: AL 

On this page

# QairtApi

Note

Some methods in this module are not yet implemented in the current release and will raise an exception if called. See the C API for full functionality.

`QairtApi.hpp` is the top-level convenience header that includes all other
QAIRT C++ API headers. It does not define any symbols of its own.

To use the QAIRT C++ API, include this header in your application:

```
#include "QairtCppApi/QairtApi.hpp"
```
See the individual sections below for the full API reference.

 Last Published: Jul 02, 2026

May contain U.S. and international export controlled information
## Extracted images

(pulled from the source doc by `.migrate/extract_images.py` -- Markdown conversion drops these; see `QairtApi - Qualcomm AI Runtime (QAIRT) SDK.mht_images/`)

- ![https://cdn.bizible.com/ipv?_biz_r=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Findex_cpp-api.html&_biz_h=78953161&_biz_u=bda1c6aa84c74aaafc0c2e845a2adbae&_biz_l=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2FQairtApi.html&_biz_t=1783659056642&_biz_i=QairtApi%20-%20Qualcomm%20AI%20Runtime%20(QAIRT)%20SDK&_biz_n=14&rnd=159513&cdn_o=a&_biz_z=1783659056643](QairtApi - Qualcomm AI Runtime (QAIRT) SDK.mht_images/mht-image-001.gif) -- https://cdn.bizible.com/ipv?_biz_r=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Findex_cpp-api.html&_biz_h=78953161&_biz_u=bda1c6aa84c74aaafc0c2e845a2adbae&_biz_l=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2FQairtApi.html&_biz_t=1783659056642&_biz_i=QairtApi%20-%20Qualcomm%20AI%20Runtime%20(QAIRT)%20SDK&_biz_n=14&rnd=159513&cdn_o=a&_biz_z=1783659056643
- ![https://cdn.bizible.com/ipv?_biz_r=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Findex_QAIRT-API.html&_biz_h=78953161&_biz_u=bda1c6aa84c74aaafc0c2e845a2adbae&_biz_l=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Findex_cpp-api.html&_biz_t=1783659035735&_biz_i=QAIRT%20C%2B%2B%20API%20-%20Qualcomm%20AI%20Runtime%20(QAIRT)%20SDK&_biz_n=13&rnd=4679&cdn_o=a&_biz_z=1783659035736](QairtApi - Qualcomm AI Runtime (QAIRT) SDK.mht_images/mht-image-002.gif) -- https://cdn.bizible.com/ipv?_biz_r=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Findex_QAIRT-API.html&_biz_h=78953161&_biz_u=bda1c6aa84c74aaafc0c2e845a2adbae&_biz_l=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Findex_cpp-api.html&_biz_t=1783659035735&_biz_i=QAIRT%20C%2B%2B%20API%20-%20Qualcomm%20AI%20Runtime%20(QAIRT)%20SDK&_biz_n=13&rnd=4679&cdn_o=a&_biz_z=1783659035736
- ![https://siteintercept.qualtrics.com/WRQualtricsShared/Graphics/siteintercept/wr-dialog-close-btn-white.png](QairtApi - Qualcomm AI Runtime (QAIRT) SDK.mht_images/mht-image-003.png) -- https://siteintercept.qualtrics.com/WRQualtricsShared/Graphics/siteintercept/wr-dialog-close-btn-white.png
- ![https://cdn.bizible.com/ipv?_biz_r=&_biz_h=78953161&_biz_u=bda1c6aa84c74aaafc0c2e845a2adbae&_biz_l=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Findex_QAIRT-API.html&_biz_t=1783659030954&_biz_i=QAIRT%20API%20-%20Qualcomm%20AI%20Runtime%20(QAIRT)%20SDK&_biz_n=12&rnd=608960&cdn_o=a&_biz_z=1783659030956](QairtApi - Qualcomm AI Runtime (QAIRT) SDK.mht_images/mht-image-004.gif) -- https://cdn.bizible.com/ipv?_biz_r=&_biz_h=78953161&_biz_u=bda1c6aa84c74aaafc0c2e845a2adbae&_biz_l=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Findex_QAIRT-API.html&_biz_t=1783659030954&_biz_i=QAIRT%20API%20-%20Qualcomm%20AI%20Runtime%20(QAIRT)%20SDK&_biz_n=12&rnd=608960&cdn_o=a&_biz_z=1783659030956
- ![https://cdn.bizible.com/ipv?_biz_r=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Fmigration-guide.html&_biz_h=78953161&_biz_u=bda1c6aa84c74aaafc0c2e845a2adbae&_biz_l=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Findex_QAIRT-API.html&_biz_t=1783659014068&_biz_i=QAIRT%20API%20Overview%20-%20Qualcomm%20AI%20Runtime%20(QAIRT)%20SDK&_biz_n=11&rnd=482974&cdn_o=a&_biz_z=1783659030955](QairtApi - Qualcomm AI Runtime (QAIRT) SDK.mht_images/mht-image-005.gif) -- https://cdn.bizible.com/ipv?_biz_r=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Fmigration-guide.html&_biz_h=78953161&_biz_u=bda1c6aa84c74aaafc0c2e845a2adbae&_biz_l=https%3A%2F%2Fdocs.qualcomm.com%2Fdoc%2F80-63442-10%2Ftopic%2Findex_QAIRT-API.html&_biz_t=1783659014068&_biz_i=QAIRT%20API%20Overview%20-%20Qualcomm%20AI%20Runtime%20(QAIRT)%20SDK&_biz_n=11&rnd=482974&cdn_o=a&_biz_z=1783659030955
- ![https://cdn.cookielaw.org/logos/static/powered_by_logo.svg](QairtApi - Qualcomm AI Runtime (QAIRT) SDK.mht_images/mht-image-006.svg) -- https://cdn.cookielaw.org/logos/static/powered_by_logo.svg
- ![https://cdn.cookielaw.org/logos/b0a5f2cc-0b29-4907-89bf-3f6b380a03c8/019b2967-1f59-7929-8629-87bcc32af336/88f57162-c334-444d-87f4-6a565e8edc19/1280px-Qualcomm-Logo.svg.png](QairtApi - Qualcomm AI Runtime (QAIRT) SDK.mht_images/mht-image-007.png) -- https://cdn.cookielaw.org/logos/b0a5f2cc-0b29-4907-89bf-3f6b380a03c8/019b2967-1f59-7929-8629-87bcc32af336/88f57162-c334-444d-87f4-6a565e8edc19/1280px-Qualcomm-Logo.svg.png
