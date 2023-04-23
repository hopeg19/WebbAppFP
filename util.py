import json


def parse_contact(query_result):
    '''
	this function jsonifies user query results
	'''
    result_list = []
    for element in query_result:
        result_list.append({'first_name': element.first_name, 'email': element.email})

    return json.dumps({'all_user': result_list})