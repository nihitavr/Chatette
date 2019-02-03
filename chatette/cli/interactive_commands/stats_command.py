"""
Module `chatette.cli.interactive_commands.stats_command`.
Contains the strategy class that represents the interactive mode command
`stats` which shows statistics about the parsing.
"""

from chatette.cli.interactive_commands.command_strategy import CommandStrategy


class StatsCommand(CommandStrategy):
    def __init__(self, command_str):
        super(StatsCommand, self).__init__(command_str)

    def execute(self, facade):
        """Implements the command `stats`, printing parsing statistics."""
        self.print_wrapper.write("Statistics:")
        stats = facade.get_stats_as_str()
        self.print_wrapper.write(stats)
