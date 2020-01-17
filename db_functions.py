import data_model


# Create Recordsets
def create_scrape(url, heading_tag, text_tag, link_tag):
    scrape_record = data_model.Scrape(url=url, heading_tag=heading_tag, text_tag=text_tag, link_tag=link_tag)
    scrape_record.save()
    return scrape_record

def create_result(url, tag, headings, text, links):
    result_record = data_model.Results(url=url, tag=tag, headings=headings, text=text, links=links)
    result_record.save()
    return result_record

# Read: (.get() and .select()) get = 1 record, select = multiple
def get_scrape(url):
    select_query = data_model.Scrape.select().where(data_model.Scrape.url == url)
    result = select_query.execute
    return result

def select_results(url):
    select_query = data_model.Results.select().where(data_model.Results.url == url)
    results = select_query.execute
    return results

# Update
def update_scrape(url):
    update_query = data_model.Scrape.update().where(data_model.Scrape.url == url)
    update_query.execute()
    return 

# Delete
def delete_scrape(url):
    delete_query = data_model.Scrape.delete().where(data_model.Scrape.url == url)

# Print results
def print_scrape(url):
    scrape = get_scrape(url)
    for s in scrape:
        print(scrape)
    return

def print_records(url):
    results = select_results(url)
    for r in results:
        print(results)
    return

