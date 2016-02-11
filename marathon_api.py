import requests, json

"""
    Marathon API https://mesosphere.github.io/marathon/docs/generated/api.html
    Author: Ioannis Petrousov
    Created: 08-Feb-16
"""

def scale_app(marathon_url, app_id, instances = 1):
    """
    Scale an application to number of instances.
    marathon_url : [string] the URL of the marathon service
    app_id : [string] ID of the running marathon app
    instances : [integer] number of instances to scale the app to
    Methon : PUT
    """

    api_endpoint = '/v2/apps/'
    headers = {'Content-Type': 'application/json'}
    payload = {'instances': instances}
    url = marathon_url + api_endpoint + app_id
    print(url)
    r = requests.put(url, data=json.dumps(payload), headers=headers)
    #TODO : Add some control based on status code
    print(r.status_code)
    return


#=====-----=====#
#=====-----=====#
#=====-----=====#


def get_nof_instances(marathon_url, app_id):
    """
    Get number of running instances given an app_id.
    marathon_url : [string] the URL of the marathon service
    app_id : [string] ID of the running marathon app
    Method : GET
    """

    api_endpoint = '/v2/apps/'
    headers = {'Content-Type': 'application/json'}
    url = marathon_url + api_endpoint + app_id
    print(url)
    r = requests.get(url, headers=headers)
    nof_instances = r.json()['app']['instances']
    print(r.status_code)
    return nof_instances



#=====-----=====#
#=====-----=====#
#=====-----=====#



def get_hosts(marathon_url, app_id):
    """
    Get IPs of hosts where the app app_id runs.
    marathon_url : [string] the URL of the marathon service
    app_id : [string] ID of the running marathon app
    Method : GET
    Return : list of host IPs
    """

    api_endpoint = '/v2/apps/'
    headers = {'Content-Type': 'application/json'}
    url = marathon_url + api_endpoint + app_id
    print(url)
    r = requests.get(url, headers=headers)
    print(r.status_code)
    hosts = []
    for h in r.json()['app']['tasks']:
        hosts.append(h['host'])
    return hosts


#=====-----=====#
#=====-----=====#
#=====-----=====#


if __name__ == '__main__':
    marathon_master = input("Enter http://<marathon ip>:<port>")
    app_name = input("Enter application name as appears on Marathon web UI")
    instances = 2

    #Uncomment to play
    #Testing purposes only
    #scale_app marathon_master, app_name, instances
    #print get_nof_instances(marathon_master, app_name)
    #print get_hosts(marathon_master, app_name)
