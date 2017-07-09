from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_mod_php(Command, Sudo):
    with Sudo():
        assert 'php' in Command('a2query -m').stdout


def test_phpinfo(Command):
    'PHP Version 7.0' in Command('curl http://localhost/phpinfo.php').stdout
