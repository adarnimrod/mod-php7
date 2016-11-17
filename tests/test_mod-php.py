def test_mod_php(Command, Sudo):
    with Sudo():
        assert 'php' in Command('a2query -m').stdout
