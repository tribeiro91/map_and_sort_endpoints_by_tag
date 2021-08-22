import json, os

def get_tags(openapi_data: dict) -> list:
    tags = []
    for tag in openapi_data.get('tags'):
        tags.append(tag.get('name'))
    return tags

def get_endpoints(openapi_data: dict) -> list:
    endpoints = []
    for path in openapi_data.get('paths'):
        path_details = openapi_data.get('paths').get(path)
        for operation in path_details:
            endpoints.append({'summary': path_details.get(operation).get('summary') ,'path': path, 'operation': operation, 'tags': path_details.get(operation).get('tags')})
    return endpoints


def sort_tags_asc(tags: list) -> list:
    new_tags_list = [None] * len(tags)
    counter = 0

    for tag in tags:        
        for correlate_tag in tags:
            if tag != correlate_tag:
                if tag > correlate_tag:
                    counter += 1
        new_tags_list[counter] = tag
        counter = 0
    
    return new_tags_list

def append_endpoints_to_tag(endpoints: list, tags: list) -> dict:
    endpoints_by_tag = {}

    for tag in tags:
        endpoints_by_tag[tag] = []
        for endpoint in endpoints:
            if tag in endpoint.get('tags'):
                endpoints_by_tag[tag].append({'path': endpoint.get('path'), 'operation':endpoint.get('operation'), 'summary': endpoint.get('summary')})
    return endpoints_by_tag


def sort_endpoints_asc_by_tag(endpoints_by_tag: dict) -> dict:
    new_endpoints_by_tag = {}
    counter = 0 

    for tag in endpoints_by_tag:
        new_endpoints_by_tag[tag] = [None] * len(endpoints_by_tag.get(tag))
        for endpoint in endpoints_by_tag.get(tag):
            for correlate_endpoint in endpoints_by_tag.get(tag):
                if endpoint != correlate_endpoint:
                    if endpoint.get('summary') > correlate_endpoint.get('summary'):
                        counter += 1
            new_endpoints_by_tag[tag][counter] = endpoint
            counter = 0
    return new_endpoints_by_tag


def main():
    with open('swagger.json', 'r') as file:
        openapi_data = json.loads(file.read())
        tags = get_tags(openapi_data)
        endpoints = get_endpoints(openapi_data)
        sorted_tags = sort_tags_asc(tags)
        endpoints_by_tag = append_endpoints_to_tag(endpoints, sorted_tags)
        sorted_endpoints_by_tag = sort_endpoints_asc_by_tag(endpoints_by_tag)

        print(sorted_endpoints_by_tag)

if __name__=="__main__":
    main()