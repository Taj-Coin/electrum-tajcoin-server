from setuptools import setup

setup(
    name="electrum-tajcoin-server",
    version="1.0",
    scripts=['run_electrum_tajcoin_server.py','electrum-tajcoin-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumtajcoinserver':'src'
        },
    py_modules=[
        'electrumtajcoinserver.__init__',
        'electrumtajcoinserver.utils',
        'electrumtajcoinserver.storage',
        'electrumtajcoinserver.deserialize',
        'electrumtajcoinserver.networks',
        'electrumtajcoinserver.blockchain_processor',
        'electrumtajcoinserver.server_processor',
        'electrumtajcoinserver.processor',
        'electrumtajcoinserver.version',
        'electrumtajcoinserver.ircthread',
        'electrumtajcoinserver.stratum_tcp',
        'electrumtajcoinserver.stratum_http'
    ],
    description="tajcoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.deg",
    maintainer="tajcoin",
    maintainer_email="support@tajcoin.org",
    license="GNU Affero GPLv3",
    url="https://github.com/tajcoin/electrum-tajcoin-server/",
    long_description="""Server for the Electrum Lightweight tajcoin Wallet"""
)


