
#生成K线表
def autoKlinTable():
    count = 0

    file = open("d:\\autoKlinTable.sql" ,"w")

    #交易所ID
    exchangeId = {21}

    #月份
    date = {6 ,7 ,8 ,9 ,10 ,11 ,12}

    #时间周期
    timeList = {"ONE_MINUTE", "THREE_MINUTE", "FIVE_MINUTE", "TEN_MINUTE", "FIFTEEN_MINUTE", "THIRTY_MINUTE",
                "SIXTY_MINUTE", "TWO_HOUR",
                "FOUR_HOUR", "SIX_HOUR", "TWELVE_HOUR", "ONE_DAY", "THREE_DAY", "ONE_WEEK", "ONE_MONTH"}
    for id in exchangeId:
        file.write("\n#=======================================================================\n")
        file.write("#===============`b_exchange_pair_kline_%d_==============================\n" % (id))
        file.write("#=======================================================================\n")
        for i in timeList:
            for j in date:
                # b_exchange_pair_kline_交易所ID_时间周期_年_月
                file.write("CREATE TABLE `b_exchange_pair_kline_%d_%s_2018_%d` (" % (id ,str(i).lower() ,j))
                file.write("\r\t`id` bigint(20) NOT NULL AUTO_INCREMENT,")
                file.write("\r\t`createDate_` datetime DEFAULT NULL COMMENT '记录创建时间',")
                file.write("\r\t`lastUpdateDate_` datetime DEFAULT NULL COMMENT '记录更新时间',")
                file.write("\r\t`version_` int(11) DEFAULT NULL COMMENT '版本',")
                file.write("\r\t`pairId_` bigint(20) DEFAULT NULL COMMENT '交易对ID',")
                file.write("\r\t`open_` double DEFAULT NULL COMMENT '价格开',")
                file.write("\r\t`close_` double DEFAULT NULL COMMENT '价格收',")
                file.write("\r\t`low_` double DEFAULT NULL COMMENT '最低价',")
                file.write("\r\t`high_` double DEFAULT NULL COMMENT '最高价',")
                file.write("\r\t`ts_` bigint(20) DEFAULT NULL COMMENT 'K线聚合粒度时间精确到分 秒数都为0',")
                file.write("\r\t`volumn_` double DEFAULT NULL COMMENT '成交量',")
                file.write("\r\tPRIMARY KEY (`id`)")
                file.write("\n) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='交易对K线数据';")
                #增加联合索引
                file.write("\ncreate index b_exchange_pair_kline_%d_%s_2018_%d_pairId_ts on b_exchange_pair_kline_%d_%s_2018_%d(pairId_,ts_);\n\n\n" % (id ,str(i).lower() ,j,id ,str(i).lower() ,j))
                file.flush()

                print("[b_exchange_pair_kline_%d_%s_2018_%d]表生成完成!" % (id ,str(i).lower() ,j) )

                #计数
                count = count + 1

    file.close()
    return count

#删除K线表
def dropKlinTable():
    count = 0

    file = open("d:\\dropKlinTable.sql", "w")

    # 交易所ID
    exchangeId = {13, 28, 3, 4, 5, 6}

    # 月份
    date = {6, 7, 8, 9, 10, 11, 12}

    # 时间周期
    timeList = {"ONE_MINUTE", "THREE_MINUTE", "FIVE_MINUTE", "TEN_MINUTE", "FIFTEEN_MINUTE", "THIRTY_MINUTE",
                "SIXTY_MINUTE", "TWO_HOUR",
                "FOUR_HOUR", "SIX_HOUR", "TWELVE_HOUR", "ONE_DAY", "THREE_DAY", "ONE_WEEK", "ONE_MONTH"}
    for id in exchangeId:
        for i in timeList:
            for j in date:
                file.write("drop table IF EXISTS`b_exchange_pair_kline_%d_%s_2018_%d`;\n" % (id, str(i).lower(), j))
                #计数
                count = count + 1

    file.close()
    return count

#删除行情历史exchangeId_字段
def dropMarketHistoryTableByexchangeId():
    count = 0

    file = open("d:\\dropMarketHistoryTableByexchangeId.sql", "w")

    # 交易所ID
    exchangeId = {13, 28, 3, 4, 5, 6}

    # 月份
    date = {6, 7, 8, 9, 10, 11, 12}
    for id in exchangeId:
            for j in date:
                file.write("alter table `b_exchange_pair_quotes_history%d_2018_%d` drop column exchangeId_;\n" % (id, j))
                #计数
                count = count + 1

    file.close()
    return count

#删除行情历史表
def dropMarketHistoryTable():
    count = 0

    file = open("d:\\dropMarketHistoryTable.sql", "w")

    # 交易所ID
    exchangeId = {13, 28, 3, 4, 5, 6}

    # 月份
    date = {6, 7, 8, 9, 10, 11, 12}
    for id in exchangeId:
            for j in date:
                file.write("drop table IF EXISTS `b_exchange_pair_quotes_history%d_2018_%d`;\n" % (id, j))
                #计数
                count = count + 1

    file.close()
    return count



#生成行情历史表
def autoMarketHistoryTableName():
    count = 0

    file = open("d:\\autoMarketHistoryTableName.sql" ,"w")

    #交易所ID
    exchangeId = {13 ,28 ,3 ,4 ,5 ,6}

    #月份
    date = {6 ,7 ,8 ,9 ,10 ,11 ,12}

    for id in exchangeId:
        file.write("#=======================================================================\n")
        file.write("#===============`b_exchange_pair_quotes_history%d_==============================\n" % (id))
        file.write("#=======================================================================\n")
        for j in date:
            # b_exchange_pair_quotes_history交易所ID_年_月
            file.write("CREATE TABLE `b_exchange_pair_quotes_history%d_2018_%d` (" % (id ,j))
            file.write("\r\t`id` bigint(20) NOT NULL AUTO_INCREMENT,")
            file.write("\r\t`createDate_` datetime DEFAULT NULL COMMENT '记录创建时间',")
            file.write("\r\t`lastUpdateDate_` datetime DEFAULT NULL COMMENT '记录更新时间',")
            file.write("\r\t`version_` int(11) DEFAULT NULL COMMENT '版本',")
            file.write("\r\t`exchangePairId_` bigint(20) DEFAULT NULL COMMENT '交易所交易对信息ID',")
            file.write("\r\t`originalPrice_` double DEFAULT NULL COMMENT '平台价格',")
            file.write("\r\t`openPrice_` double DEFAULT NULL COMMENT '开盘价',")
            file.write("\r\t`closePrice_` double DEFAULT NULL,")
            file.write("\r\t`changePercentage24H_` double DEFAULT NULL COMMENT '24小时涨跌幅',")
            file.write("\r\t`highestPrice24H_` double DEFAULT NULL COMMENT '24小时最高价格',")
            file.write("\r\t`lowestPrice24H_` double DEFAULT NULL COMMENT '24小时最低价格',")
            file.write("\r\t`turnover24H_` double DEFAULT NULL COMMENT '24小时成交额',")
            file.write("\r\t`rateUSD_` double DEFAULT NULL COMMENT '兑美元汇率',")
            file.write("\r\t`rateCNY_` double DEFAULT NULL COMMENT '兑人民币汇率',")
            file.write("\r\t`rateBTC_` double DEFAULT NULL COMMENT '兑比特币汇率',")
            file.write("\r\t`updateTime_` datetime DEFAULT NULL COMMENT '平台行情更新时间',")
            file.write("\r\t`baseCurrencyId_` int(11) DEFAULT NULL,")
            file.write("\r\t`amount_` double DEFAULT NULL,")
            file.write("\r\tPRIMARY KEY (`id`),")
            file.write("\r\tKEY `pair_id_index` (`exchangePairId_`) COMMENT '建立交易对索引'")
            file.write("\n) ENGINE=InnoDB AUTO_INCREMENT=456 DEFAULT CHARSET=utf8 COMMENT='交易所行情历史数据表';\n\n\n")
            file.flush()

            print("[b_exchange_pair_quotes_history%d_2018_%d]表生成完成!" % (id ,j) )

            #计数
            count = count + 1

    file.close()
    return count

#增加K线历史表列
def addTableColumn():
    count = 0

    file = open("d:\\addKlinTableColumn.sql", "w")

    # 交易所ID
    exchangeId = {13, 28, 3, 4, 5, 6}

    # 月份
    date = {6, 7, 8, 9, 10, 11, 12}

    # 时间周期
    timeList = {"ONE_MINUTE", "THREE_MINUTE", "FIVE_MINUTE", "TEN_MINUTE", "FIFTEEN_MINUTE", "THIRTY_MINUTE",
                "SIXTY_MINUTE", "TWO_HOUR",
                "FOUR_HOUR", "SIX_HOUR", "TWELVE_HOUR", "ONE_DAY", "THREE_DAY", "ONE_WEEK", "ONE_MONTH"}
    for id in exchangeId:
        for i in timeList:
            for j in date:
                file.write("alter table `b_exchange_pair_kline_%d_%s_2018_%d` add  column volumn_ double NULL DEFAULT NULL COMMENT '成交量';\n" % (id, str(i).lower(), j))

                # 计数
                count = count + 1

    file.close()
    return count

#增加K线历史表列
def truncateTableData():
    count = 0

    file = open("d:\\truncateTableData.sql", "w")

    # 交易所ID
    exchangeId = {13, 28, 3, 4, 5, 6}

    # 月份
    date = {6, 7, 8, 9, 10, 11, 12}

    # 时间周期
    timeList = {"ONE_MINUTE", "THREE_MINUTE", "FIVE_MINUTE", "TEN_MINUTE", "FIFTEEN_MINUTE", "THIRTY_MINUTE",
                "SIXTY_MINUTE", "TWO_HOUR",
                "FOUR_HOUR", "SIX_HOUR", "TWELVE_HOUR", "ONE_DAY", "THREE_DAY", "ONE_WEEK", "ONE_MONTH"}
    for id in exchangeId:
        for i in timeList:
            for j in date:
                file.write("truncate table b_exchange_pair_kline_%d_%s_2018_%d;\n" % (id, str(i).lower(), j))

                # 计数
                count = count + 1

    file.close()
    return count

if __name__ == "__main__":
    count = autoKlinTable()
    print("共生成[%d]张表--->K线表" % count)
    # #
    # count = dropKlinTable()
    # print("共生成[%d]张表--->删除K线表" % count)
    #
    # count = truncateTableData()
    # print("共生成[%d]张表--->清除K线表数据" % count)
    #
    # count = dropMarketHistoryTableByexchangeId()
    # print("共生成[%d]张表--->删除行情历史exchangeId_字段" % count)
    #
    # count = dropMarketHistoryTable()
    # print("共生成[%d]张表--->删除行情历史表" % count)
    #
    # count = autoMarketHistoryTableName()
    # count = dropKlinTable()
    # print("共生成[%d]张表--->生成行情历史表" % count)

    # count = addTableColumn()
    # print("共生成[%d]张表--->生成修改K线表字段" % count)
