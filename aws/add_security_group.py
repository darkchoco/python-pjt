import boto3.ec2
import getopt, sys
import collections
import csv


def update_sgs(conn, group, rule_list):
    print("Updating group \'%s\'..." % group)
    import pprint
    print("Expected Rules:")
    pprint.pprint(rule_list)

    for rule in rule_list:
        if not group.authorize(ip_protocol=rule.ip_protocol,
                               from_port=rule.from_port,
                               to_port=rule.to_port,
                               cidr_ip=rule.cidr_ip):
            print("fail to add: ip_protocol=%s, from_port=%s, to_port=%s, cidr_ip=%s)" %
                  rule.ip_protocol, rule.from_port, rule.to_port, rule.cidr_ip)


def main():
    """
    http://www.tutorialspoint.com/python/python_command_line_arguments.htm
    https://docs.python.org/3.4/library/getopt.html
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hg:i:", ["group=", "ifile="])
        if len(sys.argv) < 2:
            raise getopt.GetoptError('No arguments provided')

    except getopt.GetoptError:
        print('%s -g <Group Name> -i <Input File>' % sys.argv[0])
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('%s -g <Group Name> -i <Input File>' % sys.argv[0])
            sys.exit()
        elif opt in ("-g", "--group"):
            given_group = arg
        elif opt in ("-i", "--ifile"):
            input_file = arg
        else:
            assert False, "Unhandled option"

    conn = boto.ec2.connect_to_region("eu-west-1", profile_name='bach')
    group = conn.get_all_security_groups(groupnames=given_group)

    SecurityGroupRule = collections.namedtuple('SecurityGroupRule',
                                               ["ip_protocol", "from_port", "to_port", "cidr_ip", "src_group_name"])
    rule_list = []

    for l in csv.reader(open(input_file, 'r')):
        cidr_ip = l[0] + '/32'
        rule_list.append(SecurityGroupRule('tcp', '12013', '12013', cidr_ip, group[0].name))

    update_sgs(conn, group[0], rule_list)


if __name__ == "__main__":
    main()
