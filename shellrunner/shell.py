# -*- coding: utf-8 -*-
import paramiko


class Shell:

    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.ssh.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password)

    def close(self):
        self.ssh.close()

    def command(self, cmd):
        _, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.read(), stderr.read()
