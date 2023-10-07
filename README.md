# WORD_BOT
※このプログラムは現在開発中であり、初期段階のためコードが不十分です。また、BOTの公開予定はありません。

**Introduction**
このプログラムはReplitで作成されたDiscordBOT開発用のプログラムです。
チャットコマンドにより禁止ワードを設定し自動削除を行う、また制限されているワードをユーザーの権限ごとに管理することを目的としています。

**Feature**
主な機能は前述した通り
`!add_word [1]    //ワードをリストに追加
 !remove_word [1] //ワードをリストから削除
 Auther.OpenList  //ワードリストをチャットに公開`
上記のコマンドをDiscordのチャット内に打つことでBOTがそれぞれの命令に対応した行動をとります。
もし会話内容に禁止ワードが含まれている場合は
`f'{message.author.mention} 禁止ワードが含まれています!')`
と返します。

**Development environments**
Replit(python3-)
https://replit.com/~
UptimeRobot
https://uptimerobot.com/
