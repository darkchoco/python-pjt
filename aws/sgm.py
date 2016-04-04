#!/usr/bin/env python
import boto3.ec2
import prettytable
from argparse import ArgumentParser
import sys

__date__ = '2015-10-06'


class SecurityGroupMgr:
    def __init__(self, param, profile, region="eu-west-1"):
        self._param = param
        # http://boto.readthedocs.org/en/latest/ref/ec2.html#module-boto.ec2.connection
        self._conn = boto3.ec2.connect_to_region(region, profile_name=profile)

    @property
    def conn(self):
        return self._conn

    def show_sg_ec2_for_ip(self):
        """Show Security Group for given IP
        Each group can have several rules, which could be divided into several IPPermissions e.g. tcp(80-80),
        udp(1-65535), tcp(443-443), and so on.
        Such IPPermissions has a list named 'grants' and its member could be Group or CIDR.
        """
        table = prettytable.PrettyTable(['Id', 'Name'])  # https://code.google.com/p/prettytable/
        table.align["Id"] = "l"
        table.align["Name"] = "l"
        table.padding_width = 1

        ec2_dict = {}
        prev_group_id = None

        for group in self._conn.get_all_security_groups():
            for rule in group.rules:
                for grant in rule.grants:  # IP can belong to multiple grants
                    if grant.cidr_ip == self._param:
                        if prev_group_id != group.id:
                            table.add_row([group.id, group.name])
                            prev_group_id = group.id

                        instance_list = group.instances()
                        if len(instance_list) > 0:  # This could be possible in many cases i.e. rule without instance
                            # 처음에는 중복을 없애기 위해서 곧장 set에 넣으려고 했으나 set은 list를 가질 수 없기 때문에
                            # (list는 hashable type이 아님) dictionary로 변경
                            for inst in instance_list:
                                if inst.id not in ec2_dict:
                                    ec2_dict[inst.id] = {'Name': inst.tags['Name'], 'IP': inst.ip_address}
                                    # ec2_list.append(instance_list)  # List returned by calling group.instances()
        print('[Security Groups]')
        print(table)
        print()
        print('[EC2 Instances]')

        table = prettytable.PrettyTable(['Id', 'EC2 IP', 'Name'])  # https://code.google.com/p/prettytable/
        table.align["Id"] = "l"
        table.align["EC2 IP"] = "l"
        table.align["Name"] = "l"
        table.padding_width = 1

        for k, v in ec2_dict.items():
            table.add_row([k, v['IP'], v['Name']])

        print(table)

    def show_ec2_for_gid(self):
        pass

    def remove_ip_from_sg(self):
        pass


def main():
    """
    https://docs.python.org/3.4/library/argparse.html
    http://stackoverflow.com/a/8493862  -- very well-written brief
    http://stackoverflow.com/questions/16641502/pythons-argparse-choose-one-of-several-optional-parameter
    """
    parser = ArgumentParser()

    if len(sys.argv) < 2:
        # parser.print_usage()
        parser.print_help()
        sys.exit(1)

    subparsers = parser.add_subparsers(help='see sub-command help')

    cmd_show = subparsers.add_parser('show')
    cmd_show_grp = cmd_show.add_mutually_exclusive_group(required=True)
    cmd_show_grp.add_argument('-i', '--ip', help='show security group that IP belongs to and its instances')
    cmd_show_grp.add_argument('-g', '--group_id', help='show EC2 instances that belong to the Group ID')
    cmd_show_grp.set_defaults(subparsers='show')

    cmd_rem = subparsers.add_parser('remove')
    cmd_rem.add_argument('-r', '--remove_ip', help='remove IP from all Security Group', required=True)
    cmd_rem.set_defaults(subparsers='remove')

    args = parser.parse_args()

    # User input to get region and profile data
    region = input('Enter the region (default is \'eu-west-1\'): ')
    profile = input('Enter the profile name: ')

    if profile is None:
        print('Please enter a valid profile name')
        exit(2)

    sgm = SecurityGroupMgr(sys.argv[3], profile, region)

    if args.subparsers == 'show':
        if args.ip:
            sgm.show_sg_ec2_for_ip()
        elif args.group_id:
            print('call sgm.show_ec2_for_gid()')
            sgm.show_ec2_for_gid()
        else:
            print('Something is wrong')
    elif args.subparsers == 'remove':
        print('call sgm.remove_ip_from_sg()')
        sgm.remove_ip_from_sg()


if __name__ == "__main__":
    main()
