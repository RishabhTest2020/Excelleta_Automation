import time
from datetime import date, datetime
from gspread.exceptions import APIError
from pytz import reference
import requests
from helpers.googlesheet import *
from test_data.testdata import urls as pro_urls
from helpers.common_helpers import slack_message


def today_date():
    """
    Returns current date and time
    """
    dt = date.today()
    ht = datetime.now()
    tz = reference.LocalTimezone()
    time_zone = tz.tzname(ht)
    date_and_time = dt.strftime("%d/%m/%Y") + " " + ht.strftime("%H:%M") + " " + time_zone
    return date_and_time


def add_col_info(url, mpfc, lcps, clss, fcps, ops):
    """
    to_improve: Rishabh please add a description here
    """
    iterations = iterations_data()
    for nn in range(int(iterations) + 1):
        try:
            insert_row()
        except APIError:
            pass
    # use this math to update data in different column: (url_iter - 2) * 7 + 1
    update_cell(1, 1, 'Date')
    update_cell(1, 2, url)
    update_cell(1, 3, mpfc)
    update_cell(1, 4, lcps)
    update_cell(1, 5, clss)
    update_cell(1, 6, fcps)
    update_cell(1, 7, ops)
    format_cells("A1:N1", "blue", 50, True)


api_key = os.environ["API_KEY"]


def seo_pages_performance():
    """
    SEO pages performance test based on Google Page Speed
    """
    iterations = iterations_data()
    for u in range(2, 11):
        urls = urls_data(u)
        if urls is None:
            print(f'No Url Given in row no {u}')
            pass
        else:
            add_col_info('URL', 'max_potential_fid_score', 'largest_contentful_paint_score',
                         'cumulative_layout_shift_score', 'first_contentful_paint_score', 'overall_performance_score')
            for i in range(int(iterations)):
                # hit google lighthouse api with url to get lighthouse report and extract required data
                try:
                    lighthouse_json = requests.get(
                        f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={urls}&key={api_key}')
                    lh_response = lighthouse_json.json()
                    max_potential_fid_score = lh_response['lighthouseResult']['audits']['max-potential-fid']['score']
                except KeyError:
                    try:
                        time.sleep(100)
                        lighthouse_json = requests.get(
                            f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={urls}&key={api_key}')
                        lh_response = lighthouse_json.json()
                        max_potential_fid_score = lh_response['lighthouseResult']['audits']['max-potential-fid'][
                            'score']
                    except KeyError:
                        try:
                            time.sleep(100)
                            lighthouse_json = requests.get(
                                f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={urls}&key={api_key}')
                            lh_response = lighthouse_json.json()
                            max_potential_fid_score = lh_response['lighthouseResult']['audits']['max-potential-fid'][
                                'score']
                        except KeyError:
                            try:
                                time.sleep(80)
                                lighthouse_json = requests.get(
                                    f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={urls}&key={api_key}')
                                lh_response = lighthouse_json.json()
                                max_potential_fid_score = \
                                    lh_response['lighthouseResult']['audits']['max-potential-fid']['score']
                            except KeyError:
                                time.sleep(80)
                                lighthouse_json = requests.get(
                                    f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={urls}&key={api_key}')
                                lh_response = lighthouse_json.json()
                                max_potential_fid_score = \
                                    lh_response['lighthouseResult']['audits']['max-potential-fid'][
                                        'score']
                largest_contentful_paint_score = lh_response['lighthouseResult']['audits']['largest-contentful-paint'][
                    'score']
                cumulative_layout_shift_score = lh_response['lighthouseResult']['audits']['cumulative-layout-shift'][
                    'score']
                first_contentful_paint_score = lh_response['lighthouseResult']['audits']['first-contentful-paint'][
                    'score']
                overall_performance_score = lh_response['lighthouseResult']['categories']['performance']['score']
                # update data in google sheet
                try:
                    format_cells(f"A{i + 2}:N{i + 2}", "green", 50, True)
                    update_cell(i + 2, 1, today_date())
                    update_cell(i + 2, 2, urls)
                    update_cell(i + 2, 3, max_potential_fid_score)
                    update_cell(i + 2, 4, largest_contentful_paint_score)
                    update_cell(i + 2, 5, cumulative_layout_shift_score)
                    update_cell(i + 2, 6, first_contentful_paint_score)
                    update_cell(i + 2, 7, overall_performance_score * 100)
                except APIError:
                    time.sleep(110)
                    format_cells(f"A{i + 2}:N{i + 2}", "green", 50, True)
                    update_cell(i + 2, 1, today_date())
                    update_cell(i + 2, 2, urls)
                    update_cell(i + 2, 3, max_potential_fid_score)
                    update_cell(i + 2, 4, largest_contentful_paint_score)
                    update_cell(i + 2, 5, cumulative_layout_shift_score)
                    update_cell(i + 2, 6, first_contentful_paint_score)
                    update_cell(i + 2, 7, overall_performance_score * 100)


def seo_pages_performance_mobile():
    """
    Performance SEO test for mobile, based on Google Page Speed
    """
    iterations = iterations_data()
    for u in range(2, 11):
        urls = urls_data(u)
        if urls is None:
            print(f'No Url Given in row no {u}')
            pass
        else:
            add_col_info('URL (Mobile)', 'max_potential_fid_score (Mobile)', 'largest_contentful_paint_score (Mobile)',
                         'cumulative_layout_shift_score (Mobile)', 'first_contentful_paint_score (Mobile)',
                         'overall_performance_score (Mobile)')
            for i in range(int(iterations)):
                # hit google lighthouse api with url to get lighthouse report and extract required data for mobile site
                try:
                    lighthouse_json = requests.get(
                        f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={urls}&key={api_key}&strategy=mobile')
                    lh_response = lighthouse_json.json()
                    max_potential_fid_score = lh_response['lighthouseResult']['audits']['max-potential-fid']['score']
                except KeyError:
                    try:
                        time.sleep(100)
                        lighthouse_json = requests.get(
                            f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={urls}&key={api_key}&strategy=mobile')
                        lh_response = lighthouse_json.json()
                        max_potential_fid_score = lh_response['lighthouseResult']['audits']['max-potential-fid'][
                            'score']
                    except KeyError:
                        try:
                            time.sleep(100)
                            lighthouse_json = requests.get(
                                f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={urls}&key={api_key}&strategy=mobile')
                            lh_response = lighthouse_json.json()
                            max_potential_fid_score = lh_response['lighthouseResult']['audits']['max-potential-fid'][
                                'score']
                        except KeyError:
                            try:
                                time.sleep(80)
                                lighthouse_json = requests.get(
                                    f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={urls}&key={api_key}&strategy=mobile')
                                lh_response = lighthouse_json.json()
                                max_potential_fid_score = \
                                    lh_response['lighthouseResult']['audits']['max-potential-fid']['score']
                            except KeyError:
                                time.sleep(80)
                                lighthouse_json = requests.get(
                                    f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={urls}&key={api_key}&strategy=mobile')
                                lh_response = lighthouse_json.json()
                                max_potential_fid_score = \
                                    lh_response['lighthouseResult']['audits']['max-potential-fid'][
                                        'score']
                largest_contentful_paint_score = lh_response['lighthouseResult']['audits']['largest-contentful-paint'][
                    'score']
                cumulative_layout_shift_score = lh_response['lighthouseResult']['audits']['cumulative-layout-shift'][
                    'score']
                first_contentful_paint_score = lh_response['lighthouseResult']['audits']['first-contentful-paint'][
                    'score']
                overall_performance_score = lh_response['lighthouseResult']['categories']['performance']['score']
                # update data in google sheet
                try:
                    format_cells(f"A{i + 2}:N{i + 2}", "green", 50, True)
                    update_cell(i + 2, 1, today_date())
                    update_cell(i + 2, 2, urls)
                    update_cell(i + 2, 3, max_potential_fid_score)
                    update_cell(i + 2, 4, largest_contentful_paint_score)
                    update_cell(i + 2, 5, cumulative_layout_shift_score)
                    update_cell(i + 2, 6, first_contentful_paint_score)
                    update_cell(i + 2, 7, overall_performance_score * 100)
                except APIError:
                    format_cells(f"A{i + 2}:N{i + 2}", "green", 50, True)
                    update_cell(i + 2, 1, today_date())
                    update_cell(i + 2, 2, urls)
                    update_cell(i + 2, 3, max_potential_fid_score)
                    update_cell(i + 2, 4, largest_contentful_paint_score)
                    update_cell(i + 2, 5, cumulative_layout_shift_score)
                    update_cell(i + 2, 6, first_contentful_paint_score)
                    update_cell(i + 2, 7, overall_performance_score * 100)


def seo_performance_slack():
    """
    SEO performance test based on Google Page Speed
    Also sends a message to Slack
    """
    global max_potential_fid_score, cumulative_layout_shift_score, largest_contentful_paint_score, first_contentful_paint_score, overall_performance_score
    seo_perf_data = []
    for u in pro_urls:
        # hit google lighthouse api with url to get lighthouse report and extract required data
        try:
            lighthouse_json = requests.get(
                f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={u}&key={api_key}')
            lh_response = lighthouse_json.json()
            max_potential_fid_score = lh_response['lighthouseResult']['audits']['max-potential-fid']['score']
        except KeyError:
            try:
                time.sleep(100)
                lighthouse_json = requests.get(
                    f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={u}&key={api_key}')
                lh_response = lighthouse_json.json()
                max_potential_fid_score = lh_response['lighthouseResult']['audits']['max-potential-fid'][
                    'score']
            except KeyError:
                try:
                    time.sleep(100)
                    lighthouse_json = requests.get(
                        f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={u}&key={api_key}')
                    lh_response = lighthouse_json.json()
                    max_potential_fid_score = lh_response['lighthouseResult']['audits']['max-potential-fid'][
                        'score']
                except KeyError:
                    try:
                        time.sleep(80)
                        lighthouse_json = requests.get(
                            f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={u}&key={api_key}')
                        lh_response = lighthouse_json.json()
                        max_potential_fid_score = \
                            lh_response['lighthouseResult']['audits']['max-potential-fid']['score']
                    except KeyError:
                        time.sleep(80)
                        lighthouse_json = requests.get(
                            f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={u}&key={api_key}')
                        lh_response = lighthouse_json.json()
                        max_potential_fid_score = \
                            lh_response['lighthouseResult']['audits']['max-potential-fid'][
                                'score']
        largest_contentful_paint_score = lh_response['lighthouseResult']['audits']['largest-contentful-paint'][
            'score']
        cumulative_layout_shift_score = lh_response['lighthouseResult']['audits']['cumulative-layout-shift'][
            'score']
        first_contentful_paint_score = lh_response['lighthouseResult']['audits']['first-contentful-paint'][
            'score']
        overall_performance_score = lh_response['lighthouseResult']['categories']['performance']['score']
        seo_perf_data.append(u + ': MPFS: ' + str(max_potential_fid_score) + 's' + ', LCPS: ' +
                             str(largest_contentful_paint_score) + 's' + ', CLSS: ' + str(cumulative_layout_shift_score)
                             + 's' + ', FCPS: ' + str(first_contentful_paint_score) + 's' + ', OPS: ' +
                             str(overall_performance_score) + 's')
    print(seo_perf_data)
    perf_srt_data = str('\n'.join(seo_perf_data))
    if (max_potential_fid_score <= 1 and cumulative_layout_shift_score <= 1 and largest_contentful_paint_score <= 1
            and first_contentful_paint_score <= 1 and overall_performance_score <= 1) is True:
        slack_color = "#00FF00"
    else:
        slack_color = "#FF0000"
    slack_message(username='Promo Pages SEO Performance Report', text=str(perf_srt_data), color=slack_color)
