import os

# Basics

try:
    try:
        tid = os.environ['TID']
        login_url = os.environ['url'] + "/login" + tid
        signup_url = os.environ['url'] + "/signup" + tid
        base_url = os.environ['url'] + tid
        base_url_new = os.environ['url'] + tid
        base_url_new_pricing = os.environ['url'] + tid
        editor_url = os.environ['url'] + "/create-from" + tid
        templates_url = os.environ['url'] + "/templates" + tid
        pricing_url = os.environ['url'] + "/pricing" + tid
        publisher_url = os.environ['url'] + "/publisher" + tid
        publisher_url_new_post = os.environ['url'] + "/publisher/post/new" + tid
        my_calendar_url = os.environ['url'] + "/planner/my-calendar" + tid
        my_account = os.environ['url'] + "/settings" + tid
        ptv_url = os.environ['url'] + "/tools/photos-to-video-maker" + tid
        image_resizer_url = os.environ['url'] + "/tools/image-resizer" + tid
    except KeyError:
        login_url = os.environ['url'] + "/login"
        signup_url = os.environ['url'] + "/signup"
        base_url = os.environ['url']
        base_url_new = os.environ['url']
        base_url_new_pricing = os.environ['url']
        editor_url = os.environ['url'] + "/create-from"
        templates_url = os.environ['url'] + "/templates"
        pricing_url = os.environ['url'] + "/pricing"
        publisher_url = os.environ['url'] + "/publisher"
        publisher_url_new_post = os.environ['url'] + "/publisher/post/new"
        my_calendar_url = os.environ['url'] + "/planner/my-calendar"
        my_account = os.environ['url'] + "/settings"
        ptv_url = os.environ['url'] + "/tools/photos-to-video-maker"
        image_resizer_url = os.environ['url'] + "/tools/image-resizer"
except KeyError:
    pass

mod_header_url = 'chrome-extension://idgpnmonknjnojddfkpgkljpfnnfcklj/popup.html'
mob_header_extension_url = 'chrome://extensions/?id=idgpnmonknjnojddfkpgkljpfnnfcklj'
PTV_URL = 'https://promo.com/tools/photos-to-video-maker'
urls = ['https://promo.com/login', 'https://promo.com/tools/calendar/march', 'https://promo.com/templates']
chrome_extension_url = 'chrome://extensions/'
animation_preview_tab_A = 'https://animation-editor.int.promo.com/preview.html'
animation_preview_tab_B = 'https://animation-editor-compare.int.promo.com/preview.html'
ape_url = 'chrome-extension://aihfdmdpkhpimbjplegoicjjndhhfoej/build/index.html'

# Errors and messages
username_menu_text = "Username_menu_text"
forget_password_text = "Forgot your password?"
request_sent_text = "Request sent successfully"
promo_templates = "Promo Templates"
promo_templates2 = "Start from a beautiful template"
promo_templates3 = "Start  from scratch"
empty_textbox_message = "This field can't be empty"
wrong_creds_message = "The email or password you entered is incorrect"
vid_publish_ready = "Your video is ready!"
setting_message_my_account_success = "Changes were saved successfully."
setting_message_my_account_fail = "Changes could not be saved. Please correct the marked fields"
TEMPLATES_NOT_FOUND_MESS = r'''We couldn't find any templates that match your search for“wfdwefwef”, but don't lose hope!'''

# Titles
title_editor = "Edit Preview | Promo.com | Visual Content Creation Platform"
title_editor_raw_video = "Video Editor | Promo.com | Visual Content Creation Platform"
title_new_login = "New login Page"
title_signup_page = "Sign up free | Promo.com"
pricing_page_title = "Pricing & Plans | Promo.com | Marketing Video Maker"
pricing_page_main_text = "Unlimited. Simple. Affordable."
create_page_title = 'Create Page | Promo.com | Visual Content Creation Platform'
main_page_title = 'Video Maker | Create Videos Online | Promo.com'
editor_page_title = "Edit Preview | Promo.com | Visual Content Creation Platform"
publisher_page_title = "Promo - Publish Video"
publish_page_title = "Promo - Publish Video"
my_account_title = "My Account | Promo.com | Visual Content Creation Platform"
brand_manager_title = "Brand manager | Promo.com | Visual Content Creation Platform"
dashboard_title = "Dashboard | Promo.com | Visual Content Creation Platform"
open_promo_email_text = "Open Promo's email from your computer"
edit_vid_mail_subject = "Edit this video on your desktop"
title_templates_page = 'Video Templates | 3000+ Creative Online Video Ad Templates'
cancellation_flow_offer_title = 'Thank you for purchasing a Promo plan!'
sub_pending_title_cancel = 'Your subscription is pending cancellation'
sub_pending_title_update = 'Your subscription is pending update.'
sub_will_renew = 'Your subscription will automatically renew on'
sub_pending_title_downgrade = 'Your subscription is pending downgrade'
special_offer_title = "A special offer just for you!"
plan_cancellation_title = "Plan cancellation"
there_is_a_better_way = "There’s a better way"
special_6_months_offer_title = "Get our 6 months special"
special_1_month_offer_title = "TO BE ADDED"  # To be added
switch_to_monthly_plan = "Do you want to switch to a monthly plan?"
text_animation_word = 'PROMO TESTING'
lite_plan_offer_title = 'Before you go…'
title_image_resizer = 'Free Image Resizer | Resize Your Images Online | Promo.com'
login_title = 'Login | Promo.com'
publish_video_page = 'Promo - Publish Video'
my_calendar_title = 'Promo Planner'
social_calendar_title = "Social Media Content Calendar"
planner_title = 'Promo Planner'
ptv_lp_title = 'Photos to Video Maker | Create Dynamic Videos in Seconds |Promo.com'
ptv_dashboard_title = 'Promo.com ‑ Promo Video Maker'
shopify_title = 'QA-poland01 · Home · Shopify'
shopify_title_short = 'Shopify'

# Brand Manager Data
brand_name = 'Test Brand Promo'
brand_name2 = 'Test Brand Promo2'
brand_logo = '/files/logo-social.png'
font_path = '/files/JackSimba.otf'
green_color = '#3ABA6F'
BRAND_INFO_TEXT = {
    "brand_website": "www.promotest.com",
    "brand_phnum": "0000000000",
    "brand_address": "1234 xyz",
    "brand_fb": "promofacebook",
    "brand_insta": "promoinsta",
    "brand_twitter": "promotwitter"
}
watermark_image = '/files/logo-social.png'
logo_image = '/files/watermark.png'

# Editor uploads
upload_photo = '/files/photo1.jpg'
upload_video = '/files/Promovideo.mp4'
upload_audio = '/files/sample.mp3'

# Dashboard
drafted_video_name = 'Changed Name'

# cf_headers
cf_client_id = ('CF-Access-Client-Id', 'CF-Access-Client-Secret')
cf_client_secret = \
    ('352a2f064e280d15bf045a6c9740638c.access', '6cd0992b7b60282508def9d038f51f2371c4cf2b1a2ed6d6392868b5e4bfbd4c')

# Publisher statuses
publish_status = 'Ready to publish'
schedule_status = 'Ready to schedule'
upload_status = 'Ready to upload'
description_text_publisher = 'Promo Social Publish Testing'
description_text_scheduler = 'Promo Social Schedule Testing'
description_mobile_post = 'Promo Social Mobile View Testing'

# Keywords
pets_temps = 'pets'
home_temp = 'home'
invalid_input = 'wfdwefwef'
font_name = 'jack_simba_personal_use'
font_name_pridi = 'pridi-700'

# Geoloaction IPs

US = '135.148.4.33'
EU = '5.135.110.142'
DE = '51.75.70.34'
UK = '198.244.148.214'
PL = '146.59.14.96'
Singapur = '51.79.254.182'
Canada = '192.99.54.60'
Australia = '139.99.236.163'

create_page_google_events = ['test_event', 'create page load', 'progress screen viewed',
                             'loading page with social icons displayed',
                             'loading page with social icons displayed', 'collection tab viewed', 'search loaded',
                             'request permission to show web push displayed',
                             'request permission to show web push rejected', 'successful collection results loaded',
                             'successful video results loaded', 'filter type chosen', 'search loaded',
                             'successful collection results loaded', 'successful video results loaded',
                             'filter type chosen', 'search loaded', 'successful collection results loaded',
                             'successful video results loaded', 'filter type chosen', 'search loaded',
                             'successful video results loaded', 'successful collection results loaded', 'search loaded',
                             'remove photo selection clicked', 'search submitted from search box',
                             'successful collection results loaded', 'successful video results loaded']
create_page_mixpanel_events = ['create page load', 'test_event', 'progress screen viewed',
                               'loading page with social icons displayed',
                               'loading page with social icons displayed', 'collection tab viewed', 'search loaded',
                               'request permission to show web push displayed',
                               'request permission to show web push rejected', 'successful collection results loaded',
                               'successful video results loaded', 'filter type chosen', 'search loaded',
                               'successful collection results loaded', 'successful video results loaded',
                               'filter type chosen', 'search loaded', 'successful collection results loaded',
                               'successful video results loaded', 'filter type chosen', 'search loaded',
                               'successful video results loaded', 'successful collection results loaded',
                               'search loaded', 'remove photo selection clicked', 'search submitted from search box',
                               'successful collection results loaded', 'successful video results loaded']

ir_without_login_mixpanel_events = ['IMR homepage viewed', 'IMR image uploaded successfully',
                                    'IMR lock aspect ratio check box clicked', 'IMR resizing using custom dimensions',
                                    'IMR resizing using custom dimensions', 'IMR image downloaded button clicked',
                                    'IMR image downloaded successfully']

ir_without_login_google_events = ['IMR homepage viewed', 'IMR image uploaded successfully',
                                  'IMR lock aspect ratio check box clicked', 'IMR resizing using custom dimensions',
                                  'IMR resizing using custom dimensions', 'IMR image downloaded button clicked',
                                  'IMR image downloaded successfully']  # 7 events

ir_after_login_mixpanel_events = ['IMR homepage viewed', 'IMR image uploaded successfully',
                                  'IMR lock aspect ratio check box clicked', 'IMR category bar clicked',
                                  'IMR resizing using custom dimensions', 'IMR resizing using custom dimensions',
                                  'IMR select images check box clicked', 'IMR category bar clicked',
                                  'IMR select images check box clicked', 'IMR category bar clicked',
                                  'IMR select images check box clicked', 'IMR image downloaded button clicked',
                                  'IMR image downloaded successfully']  # 15 events

ir_after_login_google_events = ['IMR homepage viewed', 'IMR image uploaded successfully',
                                'IMR lock aspect ratio check box clicked', 'IMR category bar clicked',
                                'IMR resizing using custom dimensions', 'IMR resizing using custom dimensions',
                                'IMR select images check box clicked', 'IMR category bar clicked',
                                'IMR select images check box clicked', 'IMR category bar clicked',
                                'IMR select images check box clicked', 'IMR image downloaded button clicked',
                                'IMR image downloaded successfully']

headers_link_titles = ['June 2022 Social Media Content Calendar | Promo.com',
                       'Facebook Video Maker | Create Facebook Videos in Minutes!',
                       'Instagram Video Maker | Promo.com',
                       'YouTube Video Maker | Create Many YouTube Videos & Clips',
                       'Easy YouTube Intro Creator | Dozens of Templates | Promo.com',
                       'Real Estate Video Maker | Marketing Video Ads for Realtors',
                       'Health and Fitness Video Marketing | Create health Ads Today!',
                       'Fashion Video Ads Maker | Fashion Marketing and Promotion',
                       'Restaurant Marketing Videos | Make Promo Ads for Restaurants',
                       'Travel Video Maker | Travel Agency & Hotel Promo Video Ads',
                       'Commercial Maker - How to Make a Commercial l Promo.com',
                       'Facebook Story Ads | Facebook Story Video Ad Creator',
                       'Instagram Story Ads | Create Instagram Story Ads Easily | Promo.com',
                       'LinkedIn Video Ad Maker | Create LinkedIn Ads Easily | Promo.com',
                       'YouTube Ad Maker | Create YouTube Video Ads in minutes!',
                       'Promo Video Maker | Create Quick Promotional Videos Online',
                       'eCommerce Ads | Create eCommerce Videos Easily | Promo.com',
                       'Amazon Video Ads | Create Amazon Sponsored Ads Easily | Promo.com',
                       'Spring Ads Video Templates | Promo.com | Marketing Video Maker',
                       "Women's History Month Video Templates | Promo.com | Marketing Video Maker",
                       'Easter Video Templates | Promo.com | Marketing Video Maker',
                       'Inspirational Ad Templates | Promo.com | Marketing Video Maker',
                       'Meme Video Templates | Promo.com | Marketing Video Maker',
                       'Marketing Video Templates | Promo.com | Marketing Video Maker',
                       '6 Second Videos | Promo.com | Marketing Video Maker',
                       'Video Templates',
                       'Real Estate Video Templates | Promo.com | Marketing Video Maker',
                       'Templates for Fitness Videos | Promo.com | Marketing Video Maker',
                       'Makeup Video Presentation Templates | Promo.com | Marketing Video Maker',
                       'Restaurant Ad Templates | Promo.com | Marketing Video Maker',
                       'eCommerce Video Templates | Promo.com | Marketing Video Maker',
                       'Recruitment Video Templates | Promo.com | Marketing Video Maker',
                       'Video Templates',
                       'Facebook Video Ad Templates | Promo.com | Marketing Video Maker',
                       'Instagram Ad Templates | Promo.com | Marketing Video Maker',
                       'Video Templates',
                       'YouTube Video Ad Template | Promo.com | Marketing Video Maker',
                       'Vertical Video Templates | Promo.com | Marketing Video Maker',
                       'Meme Video Templates | Promo.com | Marketing Video Maker',
                       '6 Second Videos | Promo.com | Marketing Video Maker',
                       'Video Templates',
                       'Listicle Videos',
                       'Inspirational Ad Templates | Promo.com | Marketing Video Maker',
                       'Video Maker | Create a Video in Minutes | Promo.com',
                       'Slideshow Maker - Free Slideshow Maker | Promo.com',
                       'Easy YouTube Intro Creator | Dozens of Templates | Promo.com',
                       'Lyric Video Maker | Add Lyrics to Video | Promo.com',
                       'Ad Maker: Free Video Ads | Promo.com',
                       'Tools - Promo.com',
                       'Video Editor: Edit Videos Online | Promo.com',
                       'Add Audio to Video | Upload Audio to YouTube | Promo.com',
                       'Online Video Cutter | Cut Video Online | Promo.com',
                       'Online MP4 Editor | Edit MP4 Files Online | Promo.com',
                       'Video Compressor: Compress Video in Seconds | Promo.com',
                       'Add Text to Video Online | Text on Video | Promo.com',
                       'Free Image Resizer | Resize Your Images Online | Promo.com',
                       'Free Online Collage Maker | Collage Templates | Promo.com',
                       'Photos to Video Maker | Create Dynamic Videos in Seconds |Promo.com',
                       'YouTube Thumbnail Maker | Edit Thumbnail for YouTube | Promo.com',
                       'Montage Maker - Video Montage Maker | Promo.com',
                       'Meme Generator: Make Memes Online | Promo.com',
                       'Video to GIF Maker| How to Create a GIF | Promo.com',
                       'Add Text to GIF | GIF Maker | How to Edit a GIF | Promo.com',
                       'GIF Editor Online | How to Crop A GIF | Promo.com',
                       'Happy Birthday GIF | Promo.com',
                       'Merry Christmas GIF | Promo.com',
                       'June 2022 Social Media Content Calendar | Promo.com',
                       'Video Production Cost Estimator | Promo.com',
                       'Facebook Ad Budget Calculator | Promo.com. | Find out how much to spend',
                       'Facebook Ads Troubleshooter for Your Ad Campaigns | Promo.com',
                       'YouTube Money Calculator | Promo.com',
                       'Ebook - Promo.com',
                       'Blog - Promo.com',
                       'Promo Academy | Learn | Video Tutorials - Promo.com',
                       'Promo.com Knowledge Base',
                       'FAQ | Promo.com | Marketing Video Maker',
                       'Video Marketing 101: The Complete Guide to Succeed | Promo.com Blog',
                       'A Step-by-Step Guide To Creating Winning Videos - Promo.com',
                       "7 Things You Didn't Know You Could Do With Promo | Promo.com",
                       'How to Add Music to a Video - Song to Video | Promo.com',
                       'How to Add Subtitles to a Video | Promo.com',
                       'Aspect Ratio: Everything You Need to Know for 2022 | Promo.com']  # 82 titles

header_and_footers_links_title = ['Pricing & Plans | Promo.com | Marketing Video Maker',
                                  'About Us | Promo.com | Marketing Video Maker',
                                  'Careers - Promo.com',
                                  'Promo.com Newsroom - Promo.com',
                                  'Promo.com Affiliates Program | Promo.com',
                                  'Write For Us - Promo.com',
                                  'FAQ | Promo.com | Marketing Video Maker',
                                  'Promo.com Knowledge Base',
                                  'Blog - Promo.com',
                                  'Promo Video Maker | Create Quick Promotional Videos Online',
                                  'Commercial Maker - How to Make a Commercial l Promo.com',
                                  'Social Media Video Maker | Create Videos for Social Media',
                                  'eCommerce Ads | Create eCommerce Videos Easily | Promo.com',
                                  'Facebook Video Maker | Create Facebook Videos in Minutes!',
                                  'Facebook Video Ad Creator | Make Catchy Facebook Ads',
                                  'Facebook Story Ads | Facebook Story Video Ad Creator',
                                  'Instagram Video Maker | Promo.com',
                                  'Instagram Ad Maker | Promo.com',
                                  'Instagram Story Ads | Create Instagram Story Ads Easily | Promo.com',
                                  'YouTube Video Maker | Create Many YouTube Videos & Clips',
                                  'YouTube Ad Maker | Create YouTube Video Ads in minutes!',
                                  'Easy YouTube Intro Creator | Dozens of Templates | Promo.com',
                                  'YouTube Outro Maker | Create Outro Videos for YouTube',
                                  'LinkedIn Video Ad Maker | Create LinkedIn Ads Easily | Promo.com',
                                  'Twitter Video Ad Maker | Create Twitter Ads Easily | Promo.com',
                                  'Amazon Video Ads | Create Amazon Sponsored Ads Easily | Promo.com',
                                  'Real Estate Video Maker | Marketing Video Ads for Realtors',
                                  'Health and Fitness Video Marketing | Create health Ads Today!',
                                  'Fashion Video Ads Maker | Fashion Marketing and Promotion',
                                  'Restaurant Marketing Videos | Make Promo Ads for Restaurants',
                                  'Hair Salon Video and Promo Ideas | Cosmetic Marketing Ads',
                                  'Travel Video Maker | Travel Agency & Hotel Promo Video Ads',
                                  'Business Video Maker | Promotional Videos for Small Business',
                                  'Create inspiring videos for NPOs with a free plan | Promo.com',
                                  'Tools - Promo.com',
                                  'Photos to Video Maker | Create Dynamic Videos in Seconds |Promo.com',
                                  'Video Maker | Create a Video in Minutes | Promo.com',
                                  'Ad Maker: Free Video Ads | Promo.com',
                                  'June 2022 Social Media Content Calendar | Promo.com',
                                  'Free Image Resizer | Resize Your Images Online | Promo.com',
                                  'Free Online Collage Maker | Collage Templates | Promo.com',
                                  'Free Facebook Video Covers | Promo | Marketing Video Maker',
                                  'Video Production Cost Estimator | Promo.com',
                                  'Facebook Ad Budget Calculator | Promo.com. | Find out how much to spend',
                                  'Facebook Ads Troubleshooter for Your Ad Campaigns | Promo.com',
                                  'YouTube Money Calculator | Promo.com',
                                  'Online MP4 Editor | Edit MP4 Files Online | Promo.com',
                                  'Add Music to Video | Promo.com',
                                  'Video to GIF Maker| How to Create a GIF | Promo.com',
                                  'Add Text to GIF | GIF Maker | How to Edit a GIF | Promo.com',
                                  'Video Editor for YouTube| Online Video Maker | Promo.com',
                                  'Meme Generator: Make Memes Online | Promo.com',
                                  'Happy Birthday Video Maker | Promo.com',
                                  'Online Video Cutter | Cut Video Online | Promo.com',
                                  'Lyric Video Maker | Add Lyrics to Video | Promo.com',
                                  'Add Audio to Video | Upload Audio to YouTube | Promo.com',
                                  'Add Text to Video Online | Text on Video | Promo.com',
                                  'GIF Editor Online | How to Crop A GIF | Promo.com',
                                  'Free Online Video Merger | Merge Video Online | Promo.com',
                                  'Video Compressor: Compress Video in Seconds | Promo.com',
                                  'Video Resizer - Resize Your Videos Online | Promo.com',
                                  'YouTube Thumbnail Maker | Edit Thumbnail for YouTube | Promo.com',
                                  'Video Trimmer | Trim Your Video Online | Promo.com',
                                  'Add Subtitles to Video - Caption Maker | Promo.com',
                                  'Montage Maker - Video Montage Maker | Promo.com',
                                  'Video Cropper - Crop Video Online | Promo.com',
                                  'Slideshow Maker - Free Slideshow Maker | Promo.com',
                                  'TikTok Video Editor | TikTok for Business | Promo.com',
                                  'June 2022 Social Media Content Calendar | Promo.com',
                                  'Facebook Video Maker | Create Facebook Videos in Minutes!',
                                  'Instagram Video Maker | Promo.com',
                                  'YouTube Video Maker | Create Many YouTube Videos & Clips',
                                  'Easy YouTube Intro Creator | Dozens of Templates | Promo.com',
                                  'Real Estate Video Maker | Marketing Video Ads for Realtors',
                                  'Health and Fitness Video Marketing | Create health Ads Today!',
                                  'Fashion Video Ads Maker | Fashion Marketing and Promotion',
                                  'Restaurant Marketing Videos | Make Promo Ads for Restaurants',
                                  'Travel Video Maker | Travel Agency & Hotel Promo Video Ads',
                                  'Commercial Maker - How to Make a Commercial l Promo.com',
                                  'Facebook Story Ads | Facebook Story Video Ad Creator',
                                  'Instagram Story Ads | Create Instagram Story Ads Easily | Promo.com',
                                  'LinkedIn Video Ad Maker | Create LinkedIn Ads Easily | Promo.com',
                                  'YouTube Ad Maker | Create YouTube Video Ads in minutes!',
                                  'Promo Video Maker | Create Quick Promotional Videos Online',
                                  'eCommerce Ads | Create eCommerce Videos Easily | Promo.com',
                                  'Amazon Video Ads | Create Amazon Sponsored Ads Easily | Promo.com',
                                  'Spring Ads Video Templates | Promo.com | Marketing Video Maker',
                                  "Women's History Month Video Templates | Promo.com | Marketing Video Maker",
                                  'Easter Video Templates | Promo.com | Marketing Video Maker',
                                  'Inspirational Ad Templates | Promo.com | Marketing Video Maker',
                                  'Meme Video Templates | Promo.com | Marketing Video Maker',
                                  'Marketing Video Templates | Promo.com | Marketing Video Maker',
                                  '6 Second Videos | Promo.com | Marketing Video Maker',
                                  'Video Templates',
                                  'Real Estate Video Templates | Promo.com | Marketing Video Maker',
                                  'Templates for Fitness Videos | Promo.com | Marketing Video Maker',
                                  'Makeup Video Presentation Templates | Promo.com | Marketing Video Maker',
                                  'Restaurant Ad Templates | Promo.com | Marketing Video Maker',
                                  'eCommerce Video Templates | Promo.com | Marketing Video Maker',
                                  'Recruitment Video Templates | Promo.com | Marketing Video Maker',
                                  'Video Templates',
                                  'Facebook Video Ad Templates | Promo.com | Marketing Video Maker',
                                  'Instagram Ad Templates | Promo.com | Marketing Video Maker',
                                  'Video Templates',
                                  'YouTube Video Ad Template | Promo.com | Marketing Video Maker',
                                  'Vertical Video Templates | Promo.com | Marketing Video Maker',
                                  'Meme Video Templates | Promo.com | Marketing Video Maker',
                                  '6 Second Videos | Promo.com | Marketing Video Maker',
                                  'Video Templates',
                                  'Listicle Videos',
                                  'Inspirational Ad Templates | Promo.com | Marketing Video Maker',
                                  'Video Maker | Create a Video in Minutes | Promo.com',
                                  'Slideshow Maker - Free Slideshow Maker | Promo.com',
                                  'Easy YouTube Intro Creator | Dozens of Templates | Promo.com',
                                  'Lyric Video Maker | Add Lyrics to Video | Promo.com',
                                  'Ad Maker: Free Video Ads | Promo.com',
                                  'Tools - Promo.com',
                                  'Video Editor: Edit Videos Online | Promo.com',
                                  'Add Audio to Video | Upload Audio to YouTube | Promo.com',
                                  'Online Video Cutter | Cut Video Online | Promo.com',
                                  'Online MP4 Editor | Edit MP4 Files Online | Promo.com',
                                  'Video Compressor: Compress Video in Seconds | Promo.com',
                                  'Add Text to Video Online | Text on Video | Promo.com',
                                  'Free Image Resizer | Resize Your Images Online | Promo.com',
                                  'Free Online Collage Maker | Collage Templates | Promo.com',
                                  'Photos to Video Maker | Create Dynamic Videos in Seconds |Promo.com',
                                  'YouTube Thumbnail Maker | Edit Thumbnail for YouTube | Promo.com',
                                  'Montage Maker - Video Montage Maker | Promo.com',
                                  'Meme Generator: Make Memes Online | Promo.com',
                                  'Video to GIF Maker| How to Create a GIF | Promo.com',
                                  'Add Text to GIF | GIF Maker | How to Edit a GIF | Promo.com',
                                  'GIF Editor Online | How to Crop A GIF | Promo.com',
                                  'Happy Birthday GIF | Promo.com',
                                  'Merry Christmas GIF | Promo.com',
                                  'June 2022 Social Media Content Calendar | Promo.com',
                                  'Video Production Cost Estimator | Promo.com',
                                  'Facebook Ad Budget Calculator | Promo.com. | Find out how much to spend',
                                  'Facebook Ads Troubleshooter for Your Ad Campaigns | Promo.com',
                                  'YouTube Money Calculator | Promo.com',
                                  'Ebook - Promo.com',
                                  'Blog - Promo.com',
                                  'Promo Academy | Learn | Video Tutorials - Promo.com',
                                  'Promo.com Knowledge Base',
                                  'FAQ | Promo.com | Marketing Video Maker',
                                  'Video Marketing 101: The Complete Guide to Succeed | Promo.com Blog',
                                  'A Step-by-Step Guide To Creating Winning Videos - Promo.com',
                                  "7 Things You Didn't Know You Could Do With Promo | Promo.com",
                                  'How to Add Music to a Video - Song to Video | Promo.com',
                                  'How to Add Subtitles to a Video | Promo.com',
                                  'Aspect Ratio: Everything You Need to Know for 2022 | Promo.com']  # 150 titles
