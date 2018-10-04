/* Copyright (C) 2017 RDA Technologies Limited and/or its affiliates("RDA").
 * All rights reserved.
 *
 * This software is supplied "AS IS" without any warranties.
 * RDA assumes no responsibility or liability for the use of the software,
 * conveys no license or title under any patent, copyright, or mask work
 * right to the product. RDA reserves the right to make changes in the
 * software without notification.  RDA also make no representation or
 * warranty that such application will be suitable for the specified use
 * without further testing or modification.
 */

#include "echoserver.h"
#include <QTcpSocket>
#include <stdio.h>

EchoServer::EchoServer(QObject* parent)
    : QObject(parent),
      mSocketCount(0)
{
    mServer = new QTcpServer(this);
    connect(mServer, SIGNAL(newConnection()), this, SLOT(onNewConnection()));
}

EchoServer::~EchoServer()
{
    delete mServer;
}

bool EchoServer::startServer(quint16 port)
{
    if (mServer->listen(QHostAddress::Any, port)) {
        printf("Listen on %d successed\n", port);
        return true;
    } else {
        printf("Listen on %d failed\n", port);
        return false;
    }
}

void EchoServer::onNewConnection()
{
    QTcpSocket* socket = mServer->nextPendingConnection();
    if (socket == nullptr)
        return;

    mSocketCount++;
    printf("Connect from %s:%d count %d\n", socket->peerAddress().toString().toUtf8().constData(), socket->peerPort(), mSocketCount);
    connect(socket, SIGNAL(readyRead()), this, SLOT(onReadReady()));
    connect(socket, SIGNAL(disconnected()), this, SLOT(onDisconnected()));
}

void EchoServer::onReadReady()
{
    QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender());
    if (socket == nullptr)
        return;

    qint64 bytes = socket->bytesAvailable();
    QByteArray ba = socket->read(bytes);
    socket->write(ba);
    printf("Get %d bytes from %s:%d\n", int(bytes), socket->peerAddress().toString().toUtf8().constData(), socket->peerPort());
}

void EchoServer::onDisconnected()
{
    QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender());
    if (socket == nullptr)
        return;

    mSocketCount--;
    printf("Disconnect from %s:%d socket count %d\n", socket->peerAddress().toString().toUtf8().constData(), socket->peerPort(), mSocketCount);
    socket->deleteLater();
}
