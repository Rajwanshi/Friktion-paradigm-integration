from anchorpy import Wallet
from numpy import rec
from solana.publickey import PublicKey
import sys
from .friktion_anchor.accounts import SwapOrder, UserOrders
from .friktion_anchor.program_id import PROGRAM_ID
from .friktion_anchor.instructions import create
from solana.rpc.async_api import AsyncClient
from .constants import WHITELIST_TOKEN_MINT

class BidDetails():

    swap_order_owner: PublicKey
    order_id: PublicKey

    counterparty_give_pool: PublicKey
    counterparty_receive_pool: PublicKey

    def __init__(self,
        swap_order_owner: PublicKey,
        order_id: PublicKey,
        counterparty_give_pool: PublicKey,
        counterparty_receive_pool: PublicKey
    ):
        self.swap_order_owner = swap_order_owner
        self.order_id = order_id
        self.counterparty_give_pool = counterparty_give_pool
        self.counterparty_receive_pool = counterparty_receive_pool
