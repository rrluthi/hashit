from cement import Controller, ex
from hashit.docs.banner import VERSION_BANNER


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Hash-It String Encoder/Decoder/Hasher/Unique id string Generator'

        # text displayed at the bottom of --help output
        epilog = 'Usage: hashit command1 --foo bar'

        # controller level arguments. ex: 'hashit --version'
        arguments = [
            ### add a version banner
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @ex(
        help='example sub command1',

        # sub-command level arguments. ex: 'hashit command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-f', '--foo'],
             {'help': 'notorious foo option',
              'action': 'store',
              'dest': 'foo'}),
        ],
    )
    def command1(self):
        """Example sub-command."""

        data = {
            'foo': 'bar',
        }

        ### do something with arguments
        if self.app.pargs.foo is not None:
            data['foo'] = self.app.pargs.foo

        self.app.render(data, 'command1.jinja2')
