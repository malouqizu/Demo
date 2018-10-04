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

#include "maindialog.h"
#include "ui_maindialog.h"
#include "relaylib/usb_relay_device.h"
#include <QTcpSocket>

MainDialog::MainDialog(QWidget *parent)
    : QDialog(parent),
      ui(new Ui::MainDialog),
      mServer(nullptr),
      mDeviceInfo(nullptr)
{
    ui->setupUi(this);

    mButtons << ui->pbOpen0 << ui->pbOpen1 << ui->pbOpen2 << ui->pbOpen3
             << ui->pbOpen4 << ui->pbOpen5 << ui->pbOpen6 << ui->pbOpen7
             << ui->pbOpen8 << ui->pbOpen9 << ui->pbOpen10 << ui->pbOpen11
             << ui->pbOpen12 << ui->pbOpen13 << ui->pbOpen14 << ui->pbOpen15;
    mLabels << ui->lbName0 << ui->lbName1 << ui->lbName2 << ui->lbName3
            << ui->lbName4 << ui->lbName5 << ui->lbName6 << ui->lbName7
            << ui->lbName8 << ui->lbName9 << ui->lbName10 << ui->lbName11
            << ui->lbName12 << ui->lbName13 << ui->lbName14 << ui->lbName15;

    ui->teLog->setMaximumBlockCount(200);
    foreach (QPushButton *pb, mButtons) {
        connect(pb, SIGNAL(clicked(bool)), this, SLOT(onToggleChannel()));
    }
    connect(ui->pbScan, SIGNAL(clicked(bool)), this, SLOT(onScanDevice()));
    connect(ui->pbStart, SIGNAL(clicked(bool)), this, SLOT(onToggleServer()));

    usb_relay_init();
    onScanDevice();
    onToggleServer();
}

MainDialog::~MainDialog()
{
    if (mDeviceInfo != nullptr)
        usb_relay_device_free_enumerate(mDeviceInfo);
    usb_relay_exit();

    delete ui;
}

void MainDialog::onScanDevice()
{
    mChannels = scanChannels();

    for (int n = 0; n < mButtons.size(); n++) {
        RelayStatus oc = RELAY_NONE;
        QString name;
        if (n < mChannels.size()) {
            usb_relay_device_info *di = mChannels[n].info;
            int handle = usb_relay_device_open(mChannels[n].info);
            int ch = mChannels[n].channel;

            name = QString("%1/%2").arg((char *)di->serial_number).arg(ch + 1);
            if (handle == 0) {
                ui->teLog->appendPlainText(QString("Unable to open device: %s").arg((char *)di->serial_number));
            } else {
                unsigned int status = 0;
                if (usb_relay_device_get_status(handle, &status) != 0) {
                    ui->teLog->appendPlainText(QString("Unable to get status: %s").arg((char *)di->serial_number));
                } else {
                    oc = (status & (1 << ch)) ? RELAY_OPEN : RELAY_CLOSE;
                }
                usb_relay_device_close(handle);
            }
        }
        setChannel(n, oc, name);
    }
}

void MainDialog::setChannel(int n, RelayStatus oc, const QString &name)
{
    if (n >= mButtons.size())
        return;

    if (oc == RELAY_NONE) {
        mLabels[n]->setText(QString::number(n + 1));
        mButtons[n]->setEnabled(false);
        mButtons[n]->setText("---");
    } else if (oc == RELAY_CLOSE) {
        mLabels[n]->setText(QString("%1 - %2").arg(n + 1).arg(name));
        mButtons[n]->setEnabled(true);
        mButtons[n]->setText("Closed");
    } else {
        mLabels[n]->setText(QString("%1 - %2").arg(n + 1).arg(name));
        mButtons[n]->setEnabled(true);
        mButtons[n]->setText("Opened");
    }
}

void MainDialog::ctrlChannel(int n, RelayStatus oc)
{
    QString name;
    if (n < mChannels.size()) {
        usb_relay_device_info *di = mChannels[n].info;
        int ch = mChannels[n].channel + 1;
        name = QString("%1/%2").arg((char *)di->serial_number).arg(ch);

        int handle = usb_relay_device_open(di);
        if (handle == 0) {
            ui->teLog->appendPlainText(QString("Unable to open device: %s").arg((char *)di->serial_number));
        } else {
            if (oc == RELAY_OPEN) {
                if (usb_relay_device_open_one_relay_channel(handle, ch) != 0)
                    ui->teLog->appendPlainText(QString("Failed to open channel %1/%2").arg((char *)di->serial_number).arg(ch));
                else
                    ui->teLog->appendPlainText(QString("Open channel %1/%2").arg((char *)di->serial_number).arg(ch));
            } else if (oc == RELAY_CLOSE) {
                if (usb_relay_device_close_one_relay_channel(handle, ch) != 0)
                    ui->teLog->appendPlainText(QString("Failed to close channel %1/%2").arg((char *)di->serial_number).arg(ch));
                else
                    ui->teLog->appendPlainText(QString("Close channel %1/%2").arg((char *)di->serial_number).arg(ch));
            }
            usb_relay_device_close(handle);
        }
    }
    setChannel(n, oc, name);
}

QList<usb_relay_channel> MainDialog::scanChannels()
{
    QList<usb_relay_channel> channels;

    if (mDeviceInfo != nullptr)
        usb_relay_device_free_enumerate(mDeviceInfo);

    mDeviceInfo = usb_relay_device_enumerate();
    struct usb_relay_device_info *di = mDeviceInfo;
    while (di != nullptr) {
        ui->teLog->appendPlainText(QString("Serial number: %1 type: %2").arg((char *)di->serial_number).arg(di->type));

        int count = di->type;

        // The specified device is buggy
        if (strcmp((char *)di->serial_number, "HURTM") == 0 &&
                di->type == USB_RELAY_DEVICE_TWO_CHANNEL)
            count = USB_RELAY_DEVICE_ONE_CHANNEL;

        for (int n = 0; n < count; n++) {
            usb_relay_channel ch;
            ch.info = di;
            ch.channel = n;
            channels.push_back(ch);
        }
        di = di->next;
    }
    return channels;
}

void MainDialog::onToggleChannel()
{
    QPushButton *pb = qobject_cast<QPushButton *>(sender());
    int idx = mButtons.indexOf(pb);
    if (idx < 0)
        return;

    if (pb->text() == "Closed")
        ctrlChannel(idx, RELAY_OPEN);
    else if (pb->text() == "Opened")
        ctrlChannel(idx, RELAY_CLOSE);
}

void MainDialog::onToggleServer()
{
    if (mServer != nullptr) {
        ui->teLog->appendPlainText("Stop server");

        mServer->deleteLater();
        mServer = nullptr;
        ui->pbStart->setText("Start Server");
        ui->lePort->setEnabled(true);
    } else {
        mServer = new QTcpServer(this);
        if (!mServer->listen(QHostAddress::Any, ui->lePort->text().toInt())) {
            ui->teLog->appendPlainText("Start server failed");
            mServer->deleteLater();
            mServer = nullptr;
            return;
        }
        ui->teLog->appendPlainText("Start server successed");
        ui->pbStart->setText("Stop Server");
        ui->lePort->setEnabled(false);
        connect(mServer, SIGNAL(newConnection()), this, SLOT(onNewConnection()));
    }
}

void MainDialog::onNewConnection()
{
    if (mServer == nullptr)
        return;

    QTcpSocket *socket = mServer->nextPendingConnection();
    if (socket == nullptr)
        return;

    connect(socket, SIGNAL(readyRead()), this, SLOT(onReadyRead()));
    connect(socket, SIGNAL(disconnected()), this, SLOT(onDisconnected()));
}

void MainDialog::onReadyRead()
{
    QTcpSocket *socket = qobject_cast<QTcpSocket *>(sender());
    if (socket == nullptr)
        return;

    qint64 bytes = socket->bytesAvailable();
    QByteArray ba = socket->read(bytes);
    ui->teLog->appendPlainText(QString("Received: %1").arg(ba.constData()));

    if (ba.startsWith("open")) {
        ctrlChannel(ba.mid(5).toInt() - 1, RELAY_OPEN);
    } else if (ba.startsWith("close")) {
        ctrlChannel(ba.mid(6).toInt() - 1, RELAY_CLOSE);
    }
    socket->write("OK");
}

void MainDialog::onDisconnected()
{
    QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender());
    if (socket == nullptr)
        return;

    socket->deleteLater();
}
