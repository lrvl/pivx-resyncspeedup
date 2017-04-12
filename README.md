# pivx-resyncspeedup
PIVX:  Improve resync speed of the privacy-focused decentralized open source cryptocurrency

* Purpose Blackhole any peer with ping latency higher then 200ms.
* Improved the throughput from 100KB to a few 1MB in my area of the world.

Instructions
------------

1. Enable RPC communication in the PIVX configuration:

  ```
   ~/.pivx/pivx.conf 
   rpcuser=phi
   rpcpassword=yourpassword
   server=1
  ```
2. Start PIVX wallet

   ```
   # ./pixv-qt
   ```
3. Start the PIVX-resyncspeedup.py

   ```
   watch -n 10 'for i in $(~/pivx-resyncspeedup.py); do echo $i; sudo ip route add blackhole $i; done'
   ```
4. Enjoy higher bandwidth, see your Network Monitor window under Tools.
